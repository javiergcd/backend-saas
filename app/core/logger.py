import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)

logger = logging.getLogger(
    "backend_saas"
)