from unittest import TestCase
from unittest import main
from unittest.mock import patch
import main


class HandlerTests(TestCase):
    @patch('main.DataProvider.get_data', return_value=None)
    @patch('main.DataPresenter.show_error')
    def test_handler_shows_error_on_none_data(self, show_error, get_data):
        instance = main.Handler()
        instance.presenter.show_error = show_error
        instance.provider.get_data = get_data

        instance.handle()

        instance.presenter.show_error.assert_called_once()

    @patch('main.DataProvider.get_data', return_value="some value")
    @patch('main.DataPresenter.show_data')
    def test_handler_shows_data_on_some_data(self, show_data, get_data):
        instance = main.Handler()
        instance.presenter.show_data = show_data
        instance.provider.get_data = get_data

        instance.handle()

        instance.presenter.show_data.assert_called_once_with("some value")


if __name__ == '__main__':
    main()
