def somefunc(test):
    print('somefunc')


def shietcode(param):
    print('it must be ')


class DataProvider:
    def get_data(self):
        return "some data"


class DataPresenter:
    def show_data(self, data):
        print(data)

    def show_error(self):
        print("error")


class Handler:
    def __init__(self):
        self.provider = DataProvider()
        self.presenter = DataPresenter()

    def handle(self):
        data = self.provider.get_data()
        if data is not None:
            self.presenter.show_data(data)
        else:
            self.presenter.show_error()


if __name__ == "__main__":
    somefunc("123")
