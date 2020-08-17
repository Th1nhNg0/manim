# PUT THIS INSIDE pygments
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Punctuation


class VscodeStyle(Style):
    """
    The default style (inspired by Emacs 22).
    """

    background_color = "#1E1E1E"
    default_style = ""

    styles = {
        Punctuation: '#D4D4D4',
        Operator: "#D4D4D4",
        Comment:                'italic #6A9955',
        Keyword:                'bold #C586C0',
        Keyword.Type:                'bold #D4D4D4',
        Name:                   '#9CDCFE',
        Name.Function:          '#DCDCAA',
        Name.Attribute: '#D19A66',
        Name.Class:             'bold #0f0',
        String:                 '#CE9178',
        Number:                 '#B5CEA8',
    }
