from string import Template

FIX_TYPOS_PROMPT = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

    $text

    Return only the corrected text, don't include a preamble.
    """
)