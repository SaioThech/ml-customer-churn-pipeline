from pathlib import Path
from urllib.request import urlopen

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
OUTPUT = Path(__file__).resolve().parent / "raw" / "Telco-Customer-Churn.csv"


def download_dataset() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    print("Baixando dataset IBM Telco Customer Churn...")
    with urlopen(URL, timeout=30) as response:
        data = response.read()

    OUTPUT.write_bytes(data)
    print(f"Dataset salvo em: {OUTPUT}")
    print(f"Tamanho: {len(data):,} bytes")


if __name__ == "__main__":
    download_dataset()
