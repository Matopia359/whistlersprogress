import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox
from PySide6.QtGui import QIcon
from widget import Widget
app = QApplication(sys.argv)
window = Widget()  
window.setWindowTitle("todoist")
if sys.platform.startswith("win"):
    window.setWindowIcon(QIcon("icon.ico"))   # icon for windows Windows
else:
    window.setWindowIcon(Qicon("icon.png")) #icon for linux
    
    
frame = window.ui.todoframe
layout = QVBoxLayout()
frame.setLayout(layout) 

####| FUNCTIONS DOWN |####

def create_todo():
    newtext = window.ui.newvalue.toPlainText() #newtext is the newvalue placeholder value
    print(f"added {newtext} to the list.")
    todo = QCheckBox(newtext) # todo is the checkbox with newtext text
    layout.addWidget(todo)  #add the checkbox
    
####| FUNCTIONS UP |####



####| GADGETS DOWN  |####

window.ui.criar.clicked.connect(create_todo)  # connect the button to the function.

###| GADGETS UP |#####


window.show()  
sys.exit(app.exec())  