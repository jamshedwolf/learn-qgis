import os
import webbrowser
from PyQt5.QtWidgets import QAction, QComboBox, QLabel
from PyQt5.QtGui import QIcon

plugin_dir = os.path.dirname(__file__)

# Learning resources grouped by level
RESOURCES = {
    'Beginner': [
        {
            "title": "QGIS for Beginners",
            "url": "https://youtube.com/playlist?list=PLgxX4AQ_KUQ9oavFq9I8wZsqXW0N6VRDV&si=esrUXaYwIFX-MWdz"
        }
    ],
    'Advanced': [
        {
            "title": "Advanced QGIS Playlist",
            "url": "https://youtube.com/playlist?list=PLppGmFLhQ1HIqNiNWxVqs5wBLiA_UrKTQ&si=MjzrK_YDu-6p0tlA"
        },
        {
            "title": "Building Your First QGIS Plugin (Workshop)",
            "url": "https://youtu.be/HXaD6xyq7m0?si=dcMGnnglnIHhDDz-"
        }
    ],
    'Documentation': [
        {
            "title": "QGIS User Guide (Official)",
            "url": "https://docs.qgis.org/latest/en/docs/user_manual/"
        },
        {
            "title": "QGIS Training Manual",
            "url": "https://docs.qgis.org/latest/en/docs/training_manual/"
        },
        {
            "title": "QGIS Python API (PyQGIS)",
            "url": "https://qgis.org/pyqgis/"
        },
        {
            "title": "QGIS Developer Guide",
            "url": "https://docs.qgis.org/latest/en/docs/developers_guide/"
        }
    ]
}

class LearnQGISPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.toolbar = None

    def initGui(self):
        self.toolbar = self.iface.addToolBar('Learn QGIS Free')

        # Label for level selection
        self.label = QLabel('Level:')

        # Dropdown for Beginner / Advanced / Documentation
        self.level_selector = QComboBox()
        self.level_selector.setFixedWidth(140)
        self.level_selector.addItems(RESOURCES.keys())

        # Dropdown for link selection
        self.link_selector = QComboBox()
        self.link_selector.setFixedWidth(280)

        # Icon button to open the selected link
        icon_path = os.path.join(plugin_dir, 'logo.png')
        self.action = QAction(QIcon(icon_path), 'Open Learning Link', self.toolbar)

        # Add widgets to toolbar
        self.toolbar.addWidget(self.label)
        self.toolbar.addWidget(self.level_selector)
        self.toolbar.addWidget(self.link_selector)
        self.toolbar.addAction(self.action)

        # Setup signals
        self.level_selector.currentTextChanged.connect(self.populate_links)
        self.action.triggered.connect(self.open_link)

        # Initialize with beginner links
        self.populate_links()

    def populate_links(self):
        self.link_selector.clear()
        current_level = self.level_selector.currentText()
        for item in RESOURCES[current_level]:
            self.link_selector.addItem(item['title'])

    def open_link(self):
        current_level = self.level_selector.currentText()
        index = self.link_selector.currentIndex()
        url = RESOURCES[current_level][index]['url']
        webbrowser.open(url)

    def unload(self):
        if self.toolbar:
            del self.toolbar
