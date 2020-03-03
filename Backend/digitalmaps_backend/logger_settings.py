import logging
import colorlog
from colorlog import ColoredFormatter

"""
Cores padrões e modelo de logger para se utilizar o colorlog.
Necessário importar nas settings.
"""

formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
    datefmt=None,
    reset=True,
    style='%',
    log_colors={
        'DEBUG': 'purple',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red,bg_black',
    },
    secondary_log_colors={
        'message': {
            'ERROR': 'red',
            'CRITICAL': 'red',
            'INFO': 'purple'
        }
    }
)

logger = colorlog.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel('DEBUG')  # alterar o log level caso queira ver menos. Sobrecarrega menos a aplicação
handler.setFormatter(formatter)
logger.addHandler(handler)
