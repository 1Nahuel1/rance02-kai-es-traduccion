# Rance 02 Kai — Traducción al Español

Parche de traducción al español de **Rance 02 Kai** (AliceSoft).

Este repositorio contiene **el texto traducido y las herramientas** para generar
el AIN traducido a partir de **tu propia copia legítima del juego**. No se
distribuyen los archivos de datos del juego (AIN, ALD, DLL) ni el ejecutable:
el parche se construye en tu equipo. Solo se incluye el texto traducido, las
herramientas y un INI de configuración corregido.

[![Invítame a un café en Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/zhaskk829)

> Comprá el juego original para apoyar a sus creadores. Este es un proyecto de
> traducción hecho por aficionados y no incluye material con copyright.

## Contenido

| Archivo | Descripción |
|---|---|
| `fuente/edit_es.txt` | Traducción al español de las 7803 cadenas del juego, por ID. |
| `fuente/cache_es_v2.json` | Caché usada para regenerar la traducción sin volver a traducir todo. |
| `herramientas/aplicar_traduccion.py` | Aplica `edit_es.txt` a tu AIN original y genera el AIN traducido. |
| `config/AliceStart.ini` | INI corregido, sin la sección `[Movie]` duplicada. |
| `portproton/Rance02.exe.ppdb` | Configuración probada de PortProton. |
| `docs/VERIFICACION.md` | Estadísticas y hashes de comprobación. |

## Requisitos

- **Rance 02 Kai** original instalado.
- Python 3.10 o superior.
- Wine (el script usa `wine` para ejecutar AliceTools).
- [AliceTools](https://github.com/nunuhara/alice-tools) 0.13.0 o compatible.
- **PortProton** para jugar (recomendado; evita el problema de renderizado de
  `i`/`l` del Wine del sistema).

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/1Nahuel1/rance02-kai-es-traduccion.git
cd rance02-kai-es-traduccion
```

### 2. Generar e instalar el AIN

```bash
python3 herramientas/aplicar_traduccion.py \
  --alice /ruta/a/alice-tools-0.13.0/alice.exe \
  --game-dir "/ruta/a/Rance 02 - The Rebellious Maidens + Rance 02 Kai" \
  --install
```

El script:

- usa como base `rance02.ain.pre_es.bak` si existe; si no, `rance02.ain`;
- aplica `fuente/edit_es.txt` con AliceTools;
- corrige el ancho de `i`/`l` en el código del AIN;
- guarda backups `.pre_es.bak` de los AIN originales;
- copia el resultado a las tres rutas que usa el juego.

Si solo querés generar el archivo y copiarlo a mano:

```bash
python3 herramientas/aplicar_traduccion.py \
  --alice /ruta/a/alice-tools-0.13.0/alice.exe \
  --base-ain "/ruta/al/juego/rance02.ain" \
  --output rance02.ain.es
```

Luego copiá `rance02.ain.es` a:

- `rance02.ain`
- `Rance02.ain`
- `Rance 02 Kai script/rance02.ain`

Linux distingue mayúsculas y minúsculas, por eso hacen falta las dos variantes
en la raíz.

## Configuración de PortProton (importante)

1. Abrí PortProton y agregá `Rance02.exe`.
2. En los ajustes del juego elegí:
   - **Wine/Proton:** `PROTON_LG` (probado con `PROTON_LG_10-28`)
   - **Prefix:** `DEFAULT` (o uno dedicado)
3. También podés copiar `portproton/Rance02.exe.ppdb` junto a `Rance02.exe`.
4. Lanzá el juego **desde PortProton**, no con el Wine del sistema.

El fallo de `i`/`l` (por ejemplo `M :ra`, `m u er`, `a cue...`) no era de la
traducción: es un problema de renderizado de fuentes del Wine del sistema. Con
PortProton y `PROTON_LG_10-28` se ven correctamente palabras como
`Permíteme`, `explicando`, `llamado` y `jóvenes`.

## Errores comunes

- **El texto sigue en inglés:** falta copiar el AIN a alguna de las tres rutas,
  o el nombre no coincide exactamente.
- **`i`/`l` se ven como `:` o desaparecen:** estás usando el Wine del sistema.
  Usá PortProton con `PROTON_LG`.
- **“Fallo al inicializar el complemento DrawMovie2”:** corregido en la
  versión actual. Si usás una versión anterior, actualizá `fuente/edit_es.txt`;
  los nombres internos de los plugins no deben traducirse.
- **Error por `AliceStart.ini` / sección `[Movie]` duplicada:** usá
  `config/AliceStart.ini`.
- **El juego no arranca:** lanzalo desde PortProton y comprobá el prefix y el
  runner.

## Cómo funciona

1. AliceTools aplica `fuente/edit_es.txt` sobre el AIN original.
2. Se vuelca el código del AIN y se cambia el ancho de `i`/`l` de `3` a `6`
   en `_CalculateWidthInternal25/20/18` (`PUSH 3` → `PUSH 6`).
3. Se reensambla el AIN con el texto traducido y el ajuste de ancho.
4. Se instala en las tres rutas del juego.

## Correcciones de la versión actual

- **Plugins:** se restauraron los identificadores internos `DrawGraph` y
  `DrawMovie2`, que se habían traducido por error como `DibujarGrafico` y
  `DibujarPelicula2`. El motor no podía cargarlos y el juego mostraba
  “Fallo al inicializar el complemento DrawMovie2” o quedaba en pantalla negra.
- **Nombre de personaje:** `Silla` → `Sill` en el menú de campamento, la
  pantalla de estado y los textos de combate.
- **Menú de campamento:** `Utiliza Pertenece` → `Usar objeto` y
  `Cerrar Camperia` → `Cerrar campamento`.
- **Compatibilidad con `Ñ`:** las palabras que requerían `ñ` se reescribieron
  con sinónimos sin ese carácter (`señor` → `caballero`/`don`, `niño` → `chico`,
  `pequeño` → `chico`/`menor`, etc.) porque el motor y la codificación CP932 no
  las renderizan correctamente.
- **Longitudes:** se revisaron y reescribieron las líneas que excedían el ancho
  del cuadro de diálogo o de la narración. La comprobación final da **0**
  líneas desbordadas.
- **Verificación:** el AIN reconstruido desde el AIN original coincide byte a
  byte con el probado en PortProton.

## Verificación

El AIN generado a partir de la versión original usada en este proyecto tiene:

- Tamaño: `433367` bytes
- MD5: `c3cf4ea23847890a648803c6abee299f`
- SHA256: `885df3b24d7c31e6d54facfa3149a5e1cf93f6daffaf88c36806c32ef813111d`

Si tu copia del juego es la misma versión, el hash debería coincidir. Más
detalles en [`docs/VERIFICACION.md`](docs/VERIFICACION.md).

## Estado

- Traducción completa de las 7803 cadenas.
- Generada con Marian NMT y revisión posterior.
- Probada en PortProton con `PROTON_LG_10-28`.
- Se aceptan correcciones y mejoras de redacción.

## Apoyar el proyecto

Si la traducción te resultó útil, podés invitarme un café en Ko-fi:

**https://ko-fi.com/zhaskk829**

## Licencia y aviso legal

El código de las herramientas está bajo licencia MIT (ver `LICENSE`).

La traducción es un trabajo de aficionados. **Rance 02 Kai** y todos sus
personajes y materiales son propiedad de **AliceSoft**. Este repositorio no
incluye archivos originales del juego y no pretende sustituir a la copia
legítima. Si te gusta el juego, compralo.
