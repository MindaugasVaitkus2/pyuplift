import os
import shutil
import pytest
from pyuplift.datasets import download_lalonde_nsw


data_home = os.path.join(os.sep.join(__file__.split(os.sep)[:-1]), 'data')


def test_download_lalonde_nsw():
    download_lalonde_nsw(data_home=data_home)
    shutil.rmtree(data_home)


def test_download_lalonde_nsw__twice():
    download_lalonde_nsw(data_home=data_home)
    download_lalonde_nsw(data_home=data_home)
    shutil.rmtree(data_home)


def test_download_lalonde_nsw__wrong_control_data_url():
    with pytest.raises(Exception, match=r'.*control_data_url.*'):
        download_lalonde_nsw(control_data_url='https://users.nber.org/~rdehejia/data/nsw_control_fake.txt')


def test_download_lalonde_nsw__wrong_treated_data_url():
    with pytest.raises(Exception, match=r'.*treated_data_url.*'):
        download_lalonde_nsw(treated_data_url='https://users.nber.org/~rdehejia/data/nsw_control_fake.txt')

