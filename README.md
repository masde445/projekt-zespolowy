# Projekt zespołowy: Wycena Cięcia Laserem - DXF Analyzer

Aplikacja służąca do analizy plików DXF w celu wyceny cięcia laserem. Pozwala na obliczenie całkowitego obwodu, pola powierzchni oraz szacunkowego kosztu cięcia.

## Wprowadzenie
Aplikacja składa się z trzech głównych komponentów:
- `wycena_dxf.py`: Moduł Pythona zawierający funkcje do analizy plików DXF.
- `app.py`: Główny plik serwera Flask obsługujący interakcję z użytkownikiem.
- `index.html`, `style.css`, `script.js`: Interfejs użytkownika w formie strony internetowej.

## Instrukcja użycia
1. Uruchom serwer Flask poprzez wykonanie pliku `app.py`.
2. Przejdź do przeglądarki internetowej i otwórz stronę `http://localhost:5000`.
3. Wybierz plik DXF do analizy.
4. Wybierz z dostępnych rodzaji materiału oraz grubośći.
5. Opcjonalnie zaznacz, czy potrzebujesz materiału (ta funkcja wymaga rozbudowania, docelowo ma liczyć koszt materiału)
6. Kliknij przycisk "Analizuj plik DXF" i oczekuj na wyniki.

## Instalacja
Aby uruchomić aplikację lokalnie, wykonaj następujące kroki:
1. Sklonuj repozytorium na swój lokalny komputer: `git clone https://github.com/twoje/repozytorium.git`
2. Zainstaluj wymagane zależności, wykonując `pip install -r requirements.txt`
3. Uruchom serwer Flask poprzez wykonanie `python app.py`

## Zależności
Aplikacja wykorzystuje następujące biblioteki:
- Flask: Mikroframework do budowy aplikacji internetowych w języku Python.
- Flask-CORS: Rozszerzenie Flask do obsługi Cross-Origin Resource Sharing (CORS).
- ezdxf: Biblioteka do czytania, pisania i przetwarzania plików DXF w języku Python.

  ## Autorzy
- masde445 (https://github.com/masde445)
- MarcienD (https://github.com/MarcienD)
