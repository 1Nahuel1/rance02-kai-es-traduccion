# Fuente de la traducción

- `edit_es.txt`: traducción al español de las 7803 cadenas del juego, en el
  formato que usa AliceTools (`;s[id] = texto` / `;m[id] = texto`).
- `cache_es_v2.json`: caché de traducciones usada por el pipeline. Sirve para
  regenerar el AIN sin volver a traducir todo. Puede no reflejar los últimos
  ajustes manuales; la fuente autorizada es `edit_es.txt`.

El AIN compilado no se incluye en el repositorio. Se genera con
`herramientas/aplicar_traduccion.py` a partir de la copia original de cada
usuario.
