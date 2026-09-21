"""VRDU dataset config: per-corpus windowing defaults and the extraction
prompt template. Python (not YAML), since this holds a prompt template, not
just scalars.

Loaded by path, not imported as a package (experiment-configs' sibling
`dataset-configs/` directory name has a hyphen, so it can't be a Python
package) -- see experiments.config.load_dataset_config /
load_extraction_prompt_template.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VRDUCorpusConfig:
    corpus: str
    max_pages: int = 3
    max_chars: int = 9000


CORPORA: dict[str, VRDUCorpusConfig] = {
    "ad-buy-form": VRDUCorpusConfig(corpus="ad-buy-form", max_pages=3, max_chars=9000),
    "registration-form": VRDUCorpusConfig(corpus="registration-form", max_pages=2, max_chars=6000),
}


EXTRACTION_PROMPT_TEMPLATE = """You are extracting structured fields from a scanned government form.

FIELDS TO EXTRACT: {fields}

DOCUMENT TEXT:
\"\"\"
{document_text}
\"\"\"

Return a single JSON object mapping each field name to a list of extracted text \
value(s) as they literally appear in the document. Use an empty list for a field \
that is not present. Do not include any other keys."""
