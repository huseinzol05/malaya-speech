def load(file: str):
    from malaya_speech.model.annotation import ANNOTATION
    from malaya_speech.model.frame import SEGMENT

    try:
        import pandas as pd
    except:
        raise ValueError(
            'pandas not installed. Please install it by `pip install pandas` and try again.'
        )

    names = [
        'NA1',
        'uri',
        'NA2',
        'start',
        'duration',
        'NA3',
        'NA4',
        'speaker',
        'NA5',
        'NA6',
    ]
    dtype = {'uri': str, 'start': float, 'duration': float, 'speaker': str}
    data = pd.read_csv(
        file,
        names = names,
        dtype = dtype,
        delim_whitespace = True,
        keep_default_na = False,
    )
    annotations = {}
    for uri, turns in data.groupby('uri'):
        annotation = ANNOTATION(uri)
        for i, turn in turns.iterrows():
            segment = SEGMENT(turn['start'], turn['start'] + turn['duration'])
            annotation[segment, i] = turn['speaker']
        annotations[uri] = annotation
    return annotations
