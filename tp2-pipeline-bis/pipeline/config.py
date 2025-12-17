# pipeline/config.py
# Configuration centralisée du pipeline météo + géocodage

from pathlib import Path
from dataclasses import dataclass

# Chemins du projet
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = DATA_DIR / "reports"

# Création des dossiers s'ils n'existent pas
for dir_path in [RAW_DIR, PROCESSED_DIR, REPORTS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)


@dataclass
class APIConfig:
    """Configuration d'une API."""
    name: str
    base_url: str
    timeout: int
    rate_limit: float
    headers: dict = None
    
    def __post_init__(self):
        self.headers = self.headers or {}


# Configuration OpenMeteo (Météo)
OPENMETEO_CONFIG = APIConfig(
    name="OpenMeteo",
    base_url="https://api.open-meteo.com/v1",
    timeout=10,
    rate_limit=0.1,
    headers={"User-Agent": "IPSSI-TP-Pipeline/1.0"}
)

# Configuration API Adresse (Géocodage)
ADRESSE_CONFIG = APIConfig(
    name="API Adresse",
    base_url="https://api-adresse.data.gouv.fr",
    timeout=10,
    rate_limit=0.1,
    headers={}
)

# Paramètres d'acquisition
MAX_ITEMS = 100
BATCH_SIZE = 50

# Seuils de qualité
QUALITY_THRESHOLDS = {
    "completeness_min": 0.7,
    "geocoding_score_min": 0.5,
    "duplicates_max_pct": 5.0,
}