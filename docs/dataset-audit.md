# Candidate dataset audit

Complete this audit before treating a source as suitable for the game-versus-real comparison. The sources below are candidates, not yet approved or confirmed for the intended use.

| Source | Intended role | Labels and source details to verify | Terms and permissions | Status |
| --- | --- | --- | --- | --- |
| UrbanSound8K | Preliminary gunfire-like event-detection pilot and hard-negative examples | Confirm the `gun_shot` label meaning and recording/source grouping | Recheck dataset terms for research and demonstration | Pilot already explored; not a game-versus-real dataset |
| PUBG Gun Sound Dataset (BGG) | Candidate game-generated gunfire audio | Verify weapon/event labels, clip provenance, and grouping by original recording/session | Read repository and dataset terms; confirm permitted use and redistribution limits | Audit required |
| Kabealo et al. multi-firearm dataset | Candidate controlled real-firearm audio | Verify label schema, recording sessions, source identifiers, and download availability | Read the dataset licence and any access conditions | Audit required |

## Split and comparison notes

- Keep clips from the same original recording, session, or source in one split whenever identifiers allow.
- Record sample counts by label and source before training.
- Check whether labels are comparable across datasets and whether source identity could become a shortcut for the model.
- Do not claim a fair game-versus-real comparison if the source and recording-condition differences cannot be controlled or evaluated.
