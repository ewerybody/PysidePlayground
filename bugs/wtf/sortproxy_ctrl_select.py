import sys

from PySide6 import QtCore, QtWidgets

NAMES = 'Peter', 'Mary', 'Bobby', 'Daniel', 'Goofy', 'Allan', 'Charlie', 'Freddy'


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        hlayout = QtWidgets.QHBoxLayout(self)

        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(QtWidgets.QLabel('QTableView with QAbstractTableModel:'))
        self.tv = MyView(self)
        left_layout.addWidget(self.tv)
        hlayout.addLayout(left_layout)

        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(QtWidgets.QLabel('QTableView with QSortFilterProxyModel:'))
        search_field = QtWidgets.QLineEdit()
        self.sv = MySearchableView(self)
        search_field.textChanged.connect(self.sv.set_filter)
        right_layout.addWidget(search_field)
        right_layout.addWidget(self.sv)
        hlayout.addLayout(right_layout)


class MyView(QtWidgets.QTableView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.verticalHeader().setVisible(False)

        my_model = MyModel()
        self.setModel(my_model)

        self._sel_model = self.selectionModel()
        self._sel_model.selectionChanged.connect(self._sel_changed)

        self._sel_model.select(self.model().index(0, 0), QtCore.QItemSelectionModel.SelectionFlag.Select)

    def _sel_changed(self, item_selection: QtCore.QItemSelection):
        model = self.model()
        names = [model.data(i) for i in self._sel_model.selectedIndexes()]
        print(names)


class MySearchableView(MyView):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self._proxy = MySearchableProxy(self)
        self._proxy.setSourceModel(self.model())
        self._proxy.setDynamicSortFilter(True)
        self._proxy.setFilterCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.setModel(self._proxy)

        self._sel_model = self.selectionModel()
        self._sel_model.selectionChanged.connect(self._sel_changed)

        self._sel_model.select(self.model().index(0, 0), QtCore.QItemSelectionModel.SelectionFlag.Select)

    def set_filter(self, text):
        self._proxy.set_filter_string(text)


class MySearchableProxy(QtCore.QSortFilterProxyModel):
    def __init__(self, parent):
        super().__init__(parent)
        self._filter_string = ''
        self._filter_strings = []
        self._sel_idx = []

    def set_filter_string(self, string):
        """Handle search string for our filter function."""
        if string != self._filter_string:
            self._filter_string = string.lower()
            if ' ' in self._filter_string:
                self._filter_strings = self._filter_string.split()
            else:
                self._filter_strings = [self._filter_string]
            self.setFilterFixedString(self._filter_string)

    # These are overrides of the orignally camelCase named methods.
    # pylint: disable=invalid-name
    def filterAcceptsRow(self, source_row, source_parent):
        if not self._filter_strings:
            return True
        key = self.sourceModel().index(source_row, self.filterKeyColumn(), source_parent).data()
        return all(s in key for s in self._filter_strings)


class MyModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def rowCount(self, parent=None):
        return len(NAMES)

    def columnCount(self, parent=None):
        return 1

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return None
        return NAMES[index.row()]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec())
