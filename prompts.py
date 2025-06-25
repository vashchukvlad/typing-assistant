from string import Template


FIX_TYPOS_PROMPT = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

    $text

    Return only the corrected text, don't include a preamble.
    """
)

TRANSLATE_TO_UKRAINIAN_PROMPT = Template(
    """Переклади цей текст чи слово на українську мову:

    $text

    Якщо це можливо перекладай без пояснень або з дуже коротким поясненням.  
    """
)