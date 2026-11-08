# Verificación

## AIN generado

A partir del AIN original de la versión usada en este proyecto:

| Dato | Valor |
|---|---|
| Tamaño | `435756` bytes |
| MD5 | `db6d0e2ab5ddaf35208efebc7a718011` |
| SHA256 | `ed66f4543aba1751211471262faec238cf59d2d59872f579e0c56379531cd637` |

Si tu copia del juego es la misma versión, el AIN generado con
`herramientas/aplicar_traduccion.py` debería tener el mismo hash.

## Traducción

- Cadenas únicas: **7803**
- Traducciones reutilizadas de la caché: **6890**
- Cadenas pendientes al terminar: **0**
- Tokens/escapes alterados: **0**
- El AIN incluye el ajuste de ancho de `i`/`l` (`PUSH 3` → `PUSH 6`).
- Al reensamblar el código, AliceTools deduplica 5 IDs de cadenas repetidas.
  No afecta al texto visible.

## Fuente

| Archivo | SHA256 |
|---|---|
| `fuente/edit_es.txt` | `0e04bf0924f0ae846a4fa1e3baa81c3f0207572ddf1be59cc69db5f9e81f24c0` |
| `fuente/cache_es_v2.json` | `bc6f5c9cec8368431718d91805a2673d04f72f7c67bdbe407d58eb38d8b7eb3f` |

## Prueba de funcionamiento

- PortProton 1.7.5
- Runner: `PROTON_LG_10-28`
- Prefix: `DEFAULT`
- Resultado: diálogo en español con `i`/`l` correctos; por ejemplo
  `Permíteme`, `explicando`, `llamado`, `jóvenes`.
