import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QTextBrowser
from difflib import unified_diff

class TextDiffApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Diff Tool')
        self.setGeometry(100, 100, 800, 600)

        # 创建左右两侧的文本框
        self.textEditLeft = QTextEdit(self)
        self.textEditRight = QTextEdit(self)

        # 创建比对按钮
        diffButton = QPushButton('Compare', self)
        diffButton.clicked.connect(self.compareText)

        # 创建显示差异结果的文本框
        self.diffResultText = QTextBrowser(self)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.textEditLeft)
        layout.addWidget(self.textEditRight)
        layout.addWidget(diffButton)
        layout.addWidget(self.diffResultText)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def compareText(self):
        # 获取左右两侧文本框的文本
        textLeft = self.textEditLeft.toPlainText()
        textRight = self.textEditRight.toPlainText()

        # 进行文本差异比对
        diff_result = list(unified_diff(textLeft.splitlines(), textRight.splitlines()))

        # 将差异结果分为相同和不同的部分
        same_lines = [line[2:] for line in diff_result if line.startswith(' ')]
        diff_lines = [line[2:] for line in diff_result if line.startswith('-') or line.startswith('+')]

        # 在界面中显示相同和不同的文本
        self.diffResultText.clear()
        self.diffResultText.append("Same Lines:\n" + '\n'.join(same_lines))
        self.diffResultText.append("\nDifferent Lines:\n" + '\n'.join(diff_lines))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextDiffApp()
    ex.show()
    sys.exit(app.exec())
