#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
EDIT_FILE = BASE / "fuente" / "edit_es.txt"
DEFAULT_ALICE = Path(
    os.environ.get(
        "ALICE_EXE", "/mnt/disco_externo/alice-tools-0.13.0/alice.exe"
    )
)


def run(command, cwd):
    env = {**os.environ, "WINEDEBUG": "-all"}
    return subprocess.run(command, cwd=cwd, env=env)


def build_ain(alice, base_ain, edit_file, output):
    output.parent.mkdir(parents=True, exist_ok=True)
    print("Compilando AIN con AliceTools...")
    result = run(
        [
            "wine",
            str(alice),
            "ain",
            "edit",
            "-t",
            str(edit_file),
            "--input-encoding",
            "UTF-8",
            "-o",
            str(output),
            str(base_ain),
        ],
        cwd=alice.parent,
    )
    if result.returncode != 0:
        raise SystemExit(f"AliceTools falló con código {result.returncode}")
    if not output.exists() or output.stat().st_size == 0:
        raise SystemExit("AliceTools no generó el AIN de salida")
    fix_char_widths(alice, output)
    print(f"AIN generado: {output}")


def fix_char_widths(alice, ain_path):
    with tempfile.TemporaryDirectory(dir=ain_path.parent) as temp_dir:
        code_path = Path(temp_dir) / "code.jam"
        patched_path = Path(temp_dir) / "patched.ain"
        result = run(
            [
                "wine",
                str(alice),
                "ain",
                "dump",
                "-c",
                "-o",
                str(code_path),
                str(ain_path),
            ],
            cwd=alice.parent,
        )
        if result.returncode != 0:
            raise SystemExit("No se pudo volcar el código del AIN")
        lines = code_path.read_text(encoding="utf-8").splitlines()
        changed = 0
        for index, line in enumerate(lines):
            if line.startswith(".CASE ") and line.rstrip().endswith(
                (" 105", " 108")
            ):
                next_index = index + 1
                while next_index < len(lines) and not lines[next_index].strip():
                    next_index += 1
                if (
                    next_index < len(lines)
                    and lines[next_index].strip() == "PUSH 3"
                ):
                    lines[next_index] = "\tPUSH 6"
                    changed += 1
        if not changed:
            print("Ancho de i/l ya estaba corregido.")
            return
        code_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        result = run(
            [
                "wine",
                str(alice),
                "ain",
                "edit",
                "-c",
                str(code_path),
                "--input-encoding",
                "UTF-8",
                "-o",
                str(patched_path),
                str(ain_path),
            ],
            cwd=alice.parent,
        )
        if result.returncode != 0:
            raise SystemExit("No se pudo aplicar la corrección de ancho")
        patched_path.replace(ain_path)
        print(f"Ancho de i/l corregido ({changed} entradas).")


def backup(path):
    if path.exists() and not path.with_name(path.name + ".pre_es.bak").exists():
        shutil.copy2(path, path.with_name(path.name + ".pre_es.bak"))
        print(f"Backup: {path}.pre_es.bak")


def install(ain, game_dir):
    destinations = [
        game_dir / "rance02.ain",
        game_dir / "Rance02.ain",
        game_dir / "Rance 02 Kai script" / "rance02.ain",
    ]
    for destination in destinations:
        destination.parent.mkdir(parents=True, exist_ok=True)
        backup(destination)
        shutil.copy2(ain, destination)
        print(f"Instalado: {destination}")


def choose_base_ain(game_dir):
    candidates = [
        game_dir / "rance02.ain.pre_es.bak",
        game_dir / "rance02.ain",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise SystemExit(
        "No se encontró el AIN original. Usa --base-ain o coloca "
        "rance02.ain.pre_es.bak / rance02.ain en el juego."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Aplica la traducción española de Rance 02 Kai sobre tu copia del juego."
    )
    parser.add_argument(
        "--alice",
        type=Path,
        default=DEFAULT_ALICE,
        help="Ruta a alice.exe (AliceTools).",
    )
    parser.add_argument(
        "--game-dir",
        type=Path,
        help="Directorio del juego (donde está Rance02.exe).",
    )
    parser.add_argument(
        "--base-ain",
        type=Path,
        help="AIN original sobre el que aplicar la traducción.",
    )
    parser.add_argument(
        "--edit",
        type=Path,
        default=EDIT_FILE,
        help="Archivo edit_es.txt de la traducción.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="AIN de salida. Por defecto rance02.ain.es en el directorio actual.",
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Copia el AIN generado a las tres rutas del juego.",
    )
    args = parser.parse_args()

    alice = args.alice.resolve()
    if not alice.exists():
        raise SystemExit(f"No se encuentra AliceTools: {alice}")
    if not args.edit.exists():
        raise SystemExit(f"No se encuentra el archivo de traducción: {args.edit}")

    game_dir = args.game_dir.resolve() if args.game_dir else None
    if game_dir and not (game_dir / "Rance02.exe").exists():
        raise SystemExit(f"No se encuentra Rance02.exe en: {game_dir}")
    if args.install and not game_dir:
        raise SystemExit("--install requiere --game-dir")

    if args.base_ain:
        base_ain = args.base_ain.resolve()
    elif game_dir:
        base_ain = choose_base_ain(game_dir)
    else:
        raise SystemExit("Indica --base-ain o --game-dir")
    if not base_ain.exists():
        raise SystemExit(f"No se encuentra el AIN base: {base_ain}")

    if args.install:
        file_descriptor, temp_name = tempfile.mkstemp(
            prefix=".rance02_es_", suffix=".ain", dir=game_dir
        )
        os.close(file_descriptor)
        output = Path(temp_name)
    elif args.output:
        output = args.output.resolve()
    else:
        output = Path.cwd() / "rance02.ain.es"

    build_ain(alice, base_ain, args.edit.resolve(), output)

    if args.install:
        install(output, game_dir)
        output.unlink(missing_ok=True)
        print("\nTraducción instalada. Lanza el juego con PortProton.")
    else:
        print("\nCopia el AIN generado a las tres rutas del juego.")
        print("Lee README.md para instalar y configurar PortProton.")


if __name__ == "__main__":
    main()
