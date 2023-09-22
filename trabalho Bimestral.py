import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QLineEdit,
    QListWidget,
    QComboBox
)
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np

class Operation:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
    
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_image = None
        self.selected_operation = None
        self.operations_toDo = []
        self.colors = ["Cinza", "XYZ", "YCrCb", "HSV", "HLS", "CIE L*a*b*"]

        self.array = [
                        cv2.COLOR_BGR2GRAY,
                        cv2.COLOR_BGR2XYZ,
                        cv2.COLOR_BGR2YCrCb,
                        cv2.COLOR_BGR2HSV,
                        cv2.COLOR_BGR2HLS,
                        cv2.COLOR_BGR2LAB
                    ]

        self.default_operations =  [
            Operation("Cor", 0),
            Operation("Gaussian Blur", 5, 0), 
            Operation("Canny", 100, 200),
            Operation("Binarizar", 127, 255, cv2.THRESH_BINARY),
            Operation("Erosão", 3, 1),
            Operation("Dilatação", 3, 1)
        ]
        
        self.setWindowTitle("Trabalho Bimestral")
        self.setGeometry(100, 100, 350, 500)

        main_layout = QHBoxLayout()

        self.lateral_widget = QWidget()
        self.lateral_layout = QVBoxLayout()

        self.open_button = QPushButton("Abrir Imagem")
        self.open_button.clicked.connect(self.open_image)
        self.lateral_layout.addWidget(self.open_button)

        self.operation_list = QListWidget()
        self.operation_list.itemClicked.connect(self.get_current_operation) 
        self.lateral_layout.addWidget(self.operation_list)
        for operation in self.default_operations:
            self.operation_list.addItem(operation.name)

        self.operation_layout = QVBoxLayout()
        self.operation_layout.addWidget(QLabel("Tipo de Cor"))
        self.combobox = QComboBox()
        self.combobox.addItems(self.colors)
        self.combobox.currentIndexChanged.connect(self.selectionchange)
        self.operation_layout.addWidget(self.combobox)
        self.operation_widget = QWidget()
        self.operation_widget.setLayout(self.operation_layout)
        self.lateral_layout.addWidget(self.operation_widget)
        self.operation_widget.hide()

        self.operation_layout2 = QVBoxLayout()
        self.operation_layout2.addWidget(QLabel("Tamanho do Kernel"))
        self.kernel_size = QLineEdit()
        self.kernel_size.setText("5")
        self.kernel_size.textChanged.connect(self.selectionchange2)
        self.operation_layout2.addWidget(self.kernel_size)
        self.operation_layout2.addWidget(QLabel("Desvio Padrão"))
        self.desvio_padrao = QLineEdit()
        self.desvio_padrao.setText("0")
        self.desvio_padrao.textChanged.connect(self.selectionchange3)
        self.operation_layout2.addWidget(self.desvio_padrao)
        self.operation_widget2 = QWidget()
        self.operation_widget2.setLayout(self.operation_layout2)
        self.lateral_layout.addWidget(self.operation_widget2)
        self.operation_widget2.hide()

        self.operation_layout3 = QVBoxLayout()
        self.operation_layout3.addWidget(QLabel("Limiar Minimo"))
        self.limiar_minimo = QLineEdit()
        self.limiar_minimo.setText("100")
        self.limiar_minimo.textChanged.connect(self.selectionchange4)
        self.operation_layout3.addWidget(self.limiar_minimo)
        self.operation_layout3.addWidget(QLabel("Limiar Máximo"))
        self.limiar_maximo = QLineEdit()
        self.limiar_maximo.setText("200")
        self.limiar_maximo.textChanged.connect(self.selectionchange5)
        self.operation_layout3.addWidget(self.limiar_maximo)
        self.operation_widget3 = QWidget()
        self.operation_widget3.setLayout(self.operation_layout3)
        self.lateral_layout.addWidget(self.operation_widget3)
        self.operation_widget3.hide()

        self.operation_layout4 = QVBoxLayout()
        self.operation_layout4.addWidget(QLabel("Limiar"))
        self.limiar = QLineEdit()
        self.limiar.setText("127")
        self.limiar.textChanged.connect(self.selectionchange6)
        self.operation_layout4.addWidget(self.limiar)
        self.operation_layout4.addWidget(QLabel("Valor Máximo"))
        self.valor_maximo = QLineEdit()
        self.valor_maximo.setText("255")
        self.valor_maximo.textChanged.connect(self.selectionchange7)
        self.operation_layout4.addWidget(self.valor_maximo)
        self.operation_layout4.addWidget(QLabel("Tipo de Limiar"))
        self.tipo_limiar = QLineEdit()
        self.tipo_limiar.setText("cv2.THRESH_BINARY")
        self.operation_layout4.addWidget(self.tipo_limiar)
        self.operation_widget4 = QWidget()
        self.operation_widget4.setLayout(self.operation_layout4)
        self.lateral_layout.addWidget(self.operation_widget4)
        self.operation_widget4.hide()

        self.operation_layout5 = QVBoxLayout()
        self.operation_layout5.addWidget(QLabel("Kernel"))
        self.kernel = QLineEdit()
        self.kernel.setText("3")
        self.kernel.textChanged.connect(self.selectionchange8)
        self.operation_layout5.addWidget(self.kernel)
        self.operation_layout5.addWidget(QLabel("Iterações"))
        self.iteracoes = QLineEdit()
        self.iteracoes.setText("1")
        self.iteracoes.textChanged.connect(self.selectionchange9)
        self.operation_layout5.addWidget(self.iteracoes)
        self.operation_widget5 = QWidget()
        self.operation_widget5.setLayout(self.operation_layout5)
        self.lateral_layout.addWidget(self.operation_widget5)
        self.operation_widget5.hide()
        
        self.operation_layout6 = QVBoxLayout()
        self.operation_layout6.addWidget(QLabel("Kernel"))
        self.kernel = QLineEdit()
        self.kernel.setText("3")
        self.kernel.textChanged.connect(self.selectionchange8)
        self.operation_layout6.addWidget(self.kernel)
        self.operation_layout6.addWidget(QLabel("Iterações"))
        self.iteracoes = QLineEdit()
        self.iteracoes.setText("1")
        self.iteracoes.textChanged.connect(self.selectionchange9)
        self.operation_layout6.addWidget(self.iteracoes)
        self.operation_widget6 = QWidget()
        self.operation_widget6.setLayout(self.operation_layout6)
        self.lateral_layout.addWidget(self.operation_widget6)
        self.operation_widget6.hide()

        self.open_button = QPushButton("Aplicar Operação")
        self.open_button.clicked.connect(self.apply_operation)
        self.lateral_layout.addWidget(self.open_button)

        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.remove_item)
        self.lateral_layout.addWidget(self.history_list)

        self.clear_button = QPushButton("Limpar Histórico")
        self.clear_button.clicked.connect(self.clear_history)
        self.lateral_layout.addWidget(self.clear_button)

        self.lateral_widget.setLayout(self.lateral_layout)
        main_layout.addWidget(self.lateral_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


    def selectionchange(self, i):
        #default_operations is a tuple
        self.default_operations[0].args = (int(i),)	

    def selectionchange2(self, i):
        self.default_operations[1].args = (int(i),)
    
    def selectionchange3(self, i):
        self.default_operations[1].args = (self.default_operations[1].args[0], int(i))
    
    def selectionchange4(self, i):
        self.default_operations[2].args = (int(i),)
    
    def selectionchange5(self, i):
        self.default_operations[2].args = (self.default_operations[2].args[0], int(i))

    def selectionchange6(self, i):
        self.default_operations[3].args = (int(i),)

    def selectionchange7(self, i):
        self.default_operations[3].args = (self.default_operations[3].args[0], int(i))

    def selectionchange8(self, i):
        self.default_operations[4].args = (int(i),)

    def selectionchange9(self, i):
        self.default_operations[4].args = (self.default_operations[4].args[0], int(i))

    def get_current_operation(self, item):
        self.selected_operation = item.text()

        for obj in self.default_operations:
            if obj.name == self.selected_operation:
                self.selected_operation = obj
                break
         
        name = self.selected_operation.name
        self.operation_widget.hide()
        self.operation_widget2.hide()
        self.operation_widget3.hide()
        self.operation_widget4.hide()
        self.operation_widget5.hide()
        self.operation_widget6.hide()

        if name == "Cor":
            self.operation_widget.show()
        elif name == "Gaussian Blur":
            self.operation_widget2.show()
        elif name == "Canny":
            self.operation_widget3.show()
        elif name == "Binarizar":
            self.operation_widget4.show()
        elif name == "Erosão":
            self.operation_widget5.show()
        elif name == "Dilatação":
            self.operation_widget6.show()

    def apply_operation(self):
        if self.selected_image is not None:
            args = self.selected_operation.args
            name = self.selected_operation.name
            item_history = None

            if args is not None:
                if name == "Cor":
                    item_history = name + " " + self.colors[args[0]]
                elif name == "Gaussian Blur":
                    item_history = name
                elif name == "Canny":
                    item_history = name
                elif name == "Binarizar":
                    item_history = name
                elif name == "Erosão":
                    item_history = name
                elif name == "Dilatação":
                    item_history = name

            if item_history not in [self.history_list.item(i).text() for i in range(self.history_list.count())]:
                self.operations_toDo.append([name, [*args]])
                self.operations()

    def operations(self):
        image_copy = self.selected_image.copy()
        self.history_list.clear()

        for id in self.operations_toDo:
            name = id[0]
            args = id[1]

            if name == "Cor" and len(image_copy.shape) == 3:
                    tipo_conversao = args[0]
                    gray_image = cv2.cvtColor(image_copy, self.array[tipo_conversao])
                    image_copy = gray_image
                    self.history_list.addItem(name + " " + self.colors[tipo_conversao])

            if name == "Gaussian Blur":
                    tamanho_kernel = args[0]
                    desvio_padrao = args[1]
                    filtered_image = cv2.GaussianBlur(image_copy , (tamanho_kernel, tamanho_kernel), desvio_padrao)
                    image_copy = filtered_image
                    self.history_list.addItem(name)
                    
            if name == "Canny":
                    limiar_minimo = args[0]
                    limiar_maximo = args[1]
                    edge_image = cv2.Canny(image_copy, limiar_minimo, limiar_maximo)
                    image_copy = edge_image
                    self.history_list.addItem(name)
                
            if name == "Binarizar":
                    limiar = args[0]
                    valor_maximo = args[1]
                    tipo_limiar = args[2]
                    _, binary_image = cv2.threshold(image_copy, limiar, valor_maximo, tipo_limiar)
                    image_copy = binary_image
                    self.history_list.addItem(name)
                
            if name == "Erosão":
                    kernel = args[0]
                    iteracoes = args[1]
                    kernel = np.ones((kernel, kernel), np.uint8)
                    erosion_image = cv2.erode(image_copy, kernel, iterations=iteracoes)
                    image_copy = erosion_image
                    self.history_list.addItem(name)
                    
            if name == "Dilatação":
                    kernel = args[0]
                    iteracoes = args[1]
                    kernel = np.ones((kernel, kernel), np.uint8)
                    dilation_image = cv2.dilate(image_copy, kernel, iterations=iteracoes)
                    image_copy = dilation_image
                    self.history_list.addItem(name)
                    
        self.display_image(image_copy)

    def remove_item(self, item=None):
        index = self.history_list.row(item)
        self.history_list.takeItem(index)
        self.operations_toDo.pop(index)
        self.operations()

    def clear_history(self):
        self.operations_toDo.clear()
        self.history_list.clear()
        self.operations()

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        image_path, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.bmp *.gif);;Todos os Arquivos (*)", options=options)

        if image_path:
            try:
                self.selected_image = cv2.imread(image_path)
                self.display_image(self.selected_image)
            except Exception as e:
                print("Erro ao abrir a imagem:", str(e))
        else:
            print("Nenhuma imagem selecionada.")
    

    def display_image(self, image_copy):
        if image_copy is not None:
            cv2.imshow("Imagem", image_copy) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
