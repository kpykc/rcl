

aer_raw_event_dtype = [('timestamp', 'float'), ('x', 'int'),
                   ('y', 'int'), ('sign', 'int')]

aer_filtered_event_dtype = [
    ('timestamp', 'float'),
    ('x', 'int'),
    ('y', 'int'), ('sign', 'int'),
    ('delta', 'float'), ('frequency', 'float'),
    ('valid', 'bool'), ('same', 'bool'),
]
