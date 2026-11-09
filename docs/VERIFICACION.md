# Verificación

## AIN generado

A partir del AIN original de la versión usada en este proyecto:

| Dato | Valor |
|---|---|
| Tamaño | `433367` bytes |
| MD5 | `c3cf4ea23847890a648803c6abee299f` |
| SHA256 | `885df3b24d7c31e6d54facfa3149a5e1cf93f6daffaf88c36806c32ef813111d` |

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
- Comprobación de ancho: **0** líneas desbordadas.

## Correcciones aplicadas

- Restaurados los identificadores internos `DrawGraph` y `DrawMovie2` (antes
  traducidos como `DibujarGrafico` y `DibujarPelicula2`), que impedían cargar
  los plugins y provocaban el error de `DrawMovie2` o una pantalla negra.
- Corregido el nombre de personaje `Silla` → `Sill`.
- Corregidos `Utiliza Pertenece` → `Usar objeto` y `Cerrar Camperia` →
  `Cerrar campamento`.
- Reescritas las palabras que requerían `ñ` con sinónimos sin ese carácter
  (`señor` → `caballero`/`don`, `niño` → `chico`, `pequeño` → `chico`/`menor`,
  etc.) para que el texto sea compatible con CP932.
- Reajustadas las líneas largas para que no se corten en diálogo ni narración.

## Fuente

| Archivo | SHA256 |
|---|---|
| `fuente/edit_es.txt` | `32e2cea19b3139f2fbb9aa4b5dcd2afb1fca3dba33cd73e71d007d5832ae6d5d` |
| `fuente/cache_es_v2.json` | `544684434a787872bc2f110ab6e58d613d05212312b380abac2f601a24e09dd8` |

## Prueba de funcionamiento

- PortProton 1.7.5
- Runner: `PROTON_LG_10-28`
- Prefix: `DEFAULT`
- Resultado: arranque correcto, carga de partida, diálogo largo sin cortes y
  menú de campamento con los textos corregidos. También se ven correctamente
  `i`/`l` en palabras como `Permíteme`, `explicando`, `llamado`, `jóvenes`.
