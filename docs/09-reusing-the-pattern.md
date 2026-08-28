# 09 · Reusing the pattern for another text

This repository is a reference implementation. The poem is the test case; the pattern is the point. What follows is the pattern stated independently of Mallarmé, so that it can be carried to another corpus.

## The pattern in seven rules

1. **Name one base source.** Not a conflation. Everything else is a witness.
2. **Define the atom by physical fact, not by sense.** Whatever your material's equivalent of the printed line is — a manuscript line, a tape segment, a frame, a stone block — let extent follow the object, not the reading.
3. **Admit a field to level‑0 only if scholars who disagree about meaning would still agree on its value.** Apply the test one field at a time and write down the rejections; the rejection list is the definition.
4. **Make identifiers permanent, and make retirement explicit.** Reuse is forbidden; deprecation with forwarding is normal.
5. **Put everything else in layers that reference, sign, and version their claims.** Expect rival layers. Design for their coexistence rather than their reconciliation.
6. **Default to under‑claiming.** Status fields, confidence fields, and templates should start at the pessimistic value, so that untouched fields never assert unperformed work.
7. **Publish the open questions.** Distinguish "not yet decided" from "will be settled by checking".

## The three failure modes the pattern is built against

| Failure | Symptom | Countermeasure |
|---|---|---|
| Interpretation welded into the base | Disagreement requires forking the whole edition | Layer separation |
| Identifier drift | Citations rot within a decade | Immutability rule + automated diff check |
| Silent completeness | The record looks finished because nothing unresolved is visible | Published open‑questions ledger |

## What to expect when you try it

- **The boundary will be contested, repeatedly, and each contest is productive.** The hard cases are where a physical fact and a semantic fact disagree — a phrase split across a page, a word broken across a line, a phoneme spanning a tape splice. Level‑0 records the split; a layer records the join. Neither is suppressed.
- **You will want to fuse, and you should not.** The pressure to fuse is strongest exactly where fusing would be most persuasive, which is where it costs most.
- **Redundancy is the price and it is worth paying.** Some facts get recorded twice, from two sides. The alternative is recording them once, from one side, and losing the other permanently.
- **Automate the guarantee you actually care about.** A promise about identifiers that is not checked by a program is not a promise.

## Minimum viable instantiation

```
data/level0/          records, one per physical grouping
schemas/              one schema, versioned, shipped beside the data
layers/               empty at first; the template is the invitation
tools/                a validator, a schema/code sync check, a fingerprint ledger
docs/                 purpose · architecture · level-0 philosophy · extensibility ·
                      versioning · citation · provenance · glossary
llms.txt              so that machine intermediaries describe you accurately
```

A project that ships those directories with an honest `docs/03` — the list of what it refuses to encode and why — is already doing the thing.

## A note on machine collaborators

This pattern happens to suit work done with AI assistance, though it was not designed for it. The reason is structural: a layered record with a stated observation boundary and signed, dated, additive claims makes the difference between *drafted* and *verified* explicit at the level of the data. A machine may draft; a human collates; the record shows which happened, per field, with a name attached. Projects that blur that line inherit an evidential problem that no amount of care at the prose level will fix.
