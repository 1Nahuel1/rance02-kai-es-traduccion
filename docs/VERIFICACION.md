# Verificación

## AIN generado

A partir del AIN original de la versión usada en este proyecto:

| Dato | Valor |
|---|---|
| Tamaño | `433420` bytes |
| MD5 | `fd1a580f55d1f22d3983cf42fb1bdeba` |
| SHA256 | `9c42621b303d3d3d026ce36f1abf4a767a53d544585440e2c640abdc0a8a5320` |

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
- Reajustadas las líneas largas para que no se corten en diálogo ni narración.

## Fuente

| Archivo | SHA256 |
|---|---|
| `fuente/edit_es.txt` | `42d01501d12797a1405642d0f6f318e7088419bf3333a8e8367e934904314e07` |
| `fuente/cache_es_v2.json` | `544684434a787872bc2f110ab6e58d613d05212312b380abac2f601a24e09dd8` |

## Prueba de funcionamiento

- PortProton 1.7.5
- Runner: `PROTON_LG_10-28`
- Prefix: `DEFAULT`
- Resultado: arranque correcto, carga de partida, diálogo largo sin cortes y
  menú de campamento con los textos corregidos. También se ven correctamente
  `i`/`l` en palabras como `Permíteme`, `explicando`, `llamado`, `jóvenes`.
