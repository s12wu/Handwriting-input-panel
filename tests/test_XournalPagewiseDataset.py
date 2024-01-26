from pathlib import Path
import logging

import pytest

from src.data.online_handwriting_datasets import XournalPagewiseDataset

@pytest.mark.martin
def test_construction():

    logger = logging.getLogger('test_construction')
    logger.setLevel(logging.INFO)

    ds = XournalPagewiseDataset(
        path=Path.home() / Path('data/code/carbune2020_implementation/data/datasets/2024-01-20-xournal_dataset.xoj'),
        logger=logger
    )

@pytest.mark.martin
def test_load_data():

    logger = logging.getLogger('test_load_data')
    logger.setLevel(logging.INFO)

    ds = XournalPagewiseDataset(
        path=Path.home() / Path('data/code/carbune2020_implementation/data/datasets/2024-01-20-xournal_dataset.xoj'),
        logger=logger
    )

    ds.load_data()

    raise NotImplementedError