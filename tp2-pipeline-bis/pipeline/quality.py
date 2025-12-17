# pipeline/quality.py
# Module de scoring et rapport de qualite

import pandas as pd
from datetime import datetime
from pathlib import Path

from .config import REPORTS_DIR
from .models import QualityMetrics


class QualityAnalyzer:
    """Analyse et score la qualite des donnees."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.metrics = None
    
    def calculate_completeness(self) -> float:
        """Calcule le score de completude."""
        total_cells = self.df.size
        non_null_cells = self.df.notna().sum().sum()
        return non_null_cells / total_cells if total_cells > 0 else 0
    
    def count_duplicates(self) -> tuple[int, float]:
        """Compte les doublons."""
        id_col = self.df.columns[0]
        
        duplicates = self.df.duplicated(subset=[id_col]).sum()
        pct = duplicates / len(self.df) * 100 if len(self.df) > 0 else 0
        
        return duplicates, pct
    
    def calculate_null_counts(self) -> dict:
        """Compte les valeurs nulles par colonne."""
        return self.df.isnull().sum().to_dict()
    
    def determine_grade(self, completeness: float, duplicates_pct: float) -> str:
        """Determine la note de qualite globale."""
        score = 0
        
        score += min(completeness * 50, 50)
        
        if duplicates_pct <= 1:
            score += 50
        elif duplicates_pct <= 5:
            score += 30
        else:
            score += 10
        
        if score >= 90:
            return 'A'
        elif score >= 75:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 40:
            return 'D'
        else:
            return 'F'
    
    def analyze(self) -> QualityMetrics:
        """Effectue l'analyse complete de qualite."""
        completeness = self.calculate_completeness()
        duplicates, duplicates_pct = self.count_duplicates()
        null_counts = self.calculate_null_counts()
        
        valid_records = len(self.df) - duplicates
        
        grade = self.determine_grade(completeness, duplicates_pct)
        
        self.metrics = QualityMetrics(
            total_records=len(self.df),
            valid_records=valid_records,
            completeness_score=round(completeness, 3),
            duplicates_count=duplicates,
            duplicates_pct=round(duplicates_pct, 2),
            geocoding_success_rate=0.0,
            quality_grade=grade,
        )
        
        return self.metrics
    
    def generate_report(self, output_name: str = "quality_report") -> Path:
        """Genere un rapport de qualite en Markdown."""
        if not self.metrics:
            self.analyze()
        
        report = f"""# Rapport de Qualite des Donnees

**Genere le** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Metriques Globales

| Metrique | Valeur |
|----------|--------|
| Note globale | {self.metrics.quality_grade} |
| Total enregistrements | {self.metrics.total_records} |
| Enregistrements valides | {self.metrics.valid_records} |
| Completude | {self.metrics.completeness_score * 100:.1f}% |
| Doublons | {self.metrics.duplicates_pct:.1f}% |

## Valeurs Manquantes par Colonne

| Colonne | Valeurs nulles | % |
|---------|----------------|---|
"""
        
        for col, count in sorted(self.metrics.null_counts.items(), key=lambda x: x[1], reverse=True):
            pct = count / self.metrics.total_records * 100 if self.metrics.total_records > 0 else 0
            report += f"| {col} | {count} | {pct:.1f}% |\n"
        
        report += f"""

## Conclusion

{"Dataset acceptable pour l'analyse." if self.metrics.is_acceptable else "Dataset necessite des corrections."}

---
Rapport genere automatiquement par le pipeline
"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = REPORTS_DIR / f"{output_name}_{timestamp}.md"
        filepath.write_text(report, encoding='utf-8')
        
        print(f"Rapport sauvegarde : {filepath}")
        return filepath