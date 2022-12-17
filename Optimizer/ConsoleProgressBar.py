def progress_bar(title, current, total, bar_length=20):
    """ Zeichnet einen Fortschrittsbalken in die Konsole
    
    Zeichnet und überschreibt einen Fortschrittsbalken (Standardlänge 20 chars)
    in die Konsole. Skaliert automatisch auf 100%.

    Quelle: (C) Aravind Voggu, Stackoverflow:
    https://stackoverflow.com/questions/6169217/replace-console-output-in-python
    
    Parameters
    ----------
    title : string
        Titel der vor dem Fortschrittsbalken stehen soll
    current : int
        Aktueller Fortschrittswert
    total : int
        Maximaler Fortschrittswert
    bar_length : int
        Länge des Fortschrittsbalkens 
    """
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'{title}: [{arrow}{padding}] {int(fraction*100)}%', end=ending)