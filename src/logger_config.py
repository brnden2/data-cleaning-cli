import logging
from pathlib import Path


LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)

LOG_FILE = LOG_FOLDER / "cleaner.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)