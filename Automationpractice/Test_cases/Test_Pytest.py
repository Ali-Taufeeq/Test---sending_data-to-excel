import pytest

from Page_objects.Line_1 import Search
from Page_objects.Line_2 import Page_2
from Page_objects.Line_3rd import Country_dropdwn


@pytest.mark.usefixtures('browser')
class Test_Line1:
    def test_line_first(self):
        lined = Search(self.driver)
        lined.searching_btn()

    def test_Line2(self):
        data = Page_2(self.driver)
        data.page_2nd()

    def test_Line3(self):
        select = Country_dropdwn(self.driver)
        select.country()

