from .CsvPreparator import CsvPreparator

class PreparatorNotFoundError(Exception):
    pass

PREPARATOR_TYPE_MAP = {
    'csv': CsvPreparator
}

def create_preparator(preparator_type, **kwargs):
    if preparator_type not in PREPARATOR_TYPE_MAP:
        raise PreparatorNotFoundError('Invalid preparator type: {}'.format(preparator_type))

    prep_class = PREPARATOR_TYPE_MAP[preparator_type]
    preparator = prep_class(**kwargs)
    return preparator

__all__ = ['create_preparator']