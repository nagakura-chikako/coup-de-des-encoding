# Layer template

Copy this directory to `layers/<layer_id>/`, fill in `layer.json`, and write your annotations under `annotations/`.

## Rules

1. Reference level-0 by identifier. Never copy level-0 field values as your own assertions; never edit `data/`.
2. Pin the level-0 version you validated against in `depends_on`.
3. Sign every claim. `sigla` on the layer, or per entry if the layer has several contributors.
4. Append-only. Supersede by adding, not by editing.
5. Say what your layer does *not* claim. A layer that claims everything is not usable by anyone else.

## Annotation entry shape

```json
{
  "annotation_id": "unique_within_this_layer",
  "targets": ["tu_f6_par", "tu_f7_avance_retombee"],
  "relation": "forms_phrase",
  "claim": "Prose statement of what is being asserted.",
  "confidence": "asserted | proposed | speculative",
  "sigla": "N",
  "date": "YYYY-MM-DD",
  "supersedes": null
}
```

`relation` is free vocabulary per layer, but declare it in your README. Do not overload the level-0 vocabulary with new meanings.

## If your layer cannot be expressed without changing level-0

Stop and file an open question. That situation is informative and the project wants to hear about it.
