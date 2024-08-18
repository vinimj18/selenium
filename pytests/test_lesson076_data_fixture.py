import pytest
from pytests.base_class import BaseClass


@pytest.mark.usefixtures('data_load')
class TestData(BaseClass):
    def test_edit_profile(self, data_load):
        log = self.get_logger()
        log.info(data_load[0])
        log.info(data_load[2])
