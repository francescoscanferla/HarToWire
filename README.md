# HAR to WireMock Converter

Questo progetto converte i file HAR (HTTP Archive) in file di mapping WireMock JSON.

## Requisiti

- Python 3.x

## Installazione

1. Clona questo repository:
    ```sh
    git clone <URL_DEL_REPOSITORY>
    cd har-to-wire
    ```

2. Installa le dipendenze (se presenti):
    ```sh
    pip install -r requirements.txt
    ```

## Utilizzo

Esegui lo script [main.py](http://_vscodecontentref_/1) passando il percorso del file HAR e un prefisso opzionale per i file di output:
```sh
python main.py <file_har> <prefisso_file>
