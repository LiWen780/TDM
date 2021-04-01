import tkinter
import json
import math

#The list class-------------------------------------------------------------------------------------------------------
class List:
    def __init__(self):
        self.type = "list"
        self.data = []
 
    def add(self,element):
        self.data.append(element)
        
    def addAll(self, array):
        if type(array) is list:
            for i in array:
                self.data.append(i);
        else:
            print("This is not an array")
    
    def update(self,at,element):
        if type(at) is int:
            if len(self.data) > at:
                self.data[at] = element
            else:
                print("The address "+str(at)+" doesn't exist in the List.")
        else:
            print(str(at)+" is not a number")
            
    def clear(self):
        self.data.clear()
        
    def size(self):
        return len(self.data)
        
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def get(self, index):
        if type(index) is int:
            if len(self.data) > index:
                return self.data[index]
            else:
                print("The address "+str(at)+" doesn't exist in the List.")
                return None
        else:
            print(str(at)+" is not a number.")
            return None
       
    def contain(self, element):
        value = False
        for i in self.data:
            if i == element:
                value = True
                break
        return value
        
    def remove(self, index):
        if type(index) is int:
            if len(self.data) > index:
                self.data.pop(index)
            else:
                print("The index "+str(index)+" doesn't exist in the List.")
        else:
            print("The index "+str(index)+" is not a number.")
    
    def indexOf(self, element):
        return self.data.index(element)
        
        
#The Table class-------------------------------------------------------------------------------------------------------------------------
class Table:
    def __init__(self):
        self.type = "table"
        self._max_column = 0
        self._max_row = 0
        self.column = {}
    
    def addColumn(self,name):
        if (type(name) is str) or (type(name) is int) or (type(name) is bool):
            self.column[name] = []
            self._max_column = len(self.column)
        elif type(name) is list:
            for j in name:
                if (type(j) is str) or (type(j) is int) or (type(j) is bool):
                    self.column[j] = []
            self._max_column = len(self.column)
        
    def addRow(self, col_name, element):
        if (type(col_name) is str) or (type(col_name) is int) or (type(col_name) is bool):
            if type(element) is not list:
                self.column[col_name].append(element)
                if len(self.column) > self._max_column:
                    self._max_column = len(self.column)
            else:
                for k in element:
                    self.column[col_name].append(k)
                if len(self.column) > self._max_column:
                    self._max_column = len(self.column)
    
    def updateRow(self, col_name, ro_index, new_value):
        if (type(col_name) is str) or (type(col_name) is int) or (type(col_name) is bool):
            if col_name in self.column:
                if (type(ro_index) is int) and (ro_index < len(self.column[col_name])):
                    self.column[col_name][ro_index] = new_value
    
    def updateColumn(self, col_name, new_name):
        if (type(col_name) is str) or (type(col_name) is int) or (type(col_name) is bool):
            self.column[new_name] = self.column[col_name]
            del self.column[col_name]
    
    def removeColumn(self, col_name):
        if (type(col_name) is str) or (type(col_name) is int) or (type(col_name) is bool):
            del self.column[col_name]
    
    def removeRow(self, row_index):
        if type(row_index) is int:
            for m in list(self.column):
                if row_index < len(self.column[m]):
                    self.column[m].pop(row_index)
    
    def getData(self, col_name, ro_index):
        if (type(col_name) is str) or (type(col_name) is int) or (type(col_name) is bool):
            if (type(ro_index) is int) and (ro_index < len(self.column[col_name])):
                return self.column[col_name][ro_index]
            else:
                return ""
        else:
            return ""
    
    def display(self):
        root = tkinter.Tk()
        root.title("TDM")
        k = 0
        c = 0
        r = 0
        for i in list(self.column):
            t = tkinter.Entry(root, width = 20, fg = 'white', bg = 'black', justify = 'center', font = ('Arial',16,'bold'))
            t.grid(row = r, column = c)
            t.insert(k, i)
            t.config(state='disabled', disabledforeground="white",disabledbackground="black")
            
            r = r + 1
            k = k + 1
            
            for j in self.column[i]:
                e = tkinter.Entry(root, width = 20, fg = 'blue', justify = 'center', font = ('Arial',16,'bold'))

                e.grid(row=r, column=c)
                e.insert(k, j)
                e.config(state='disabled', disabledforeground="blue",disabledbackground="white")
                
                r = r + 1
                k = k + 1
            r = 0
            c = c + 1

        root.mainloop()
        
    def saveTable(self, file_name):
        if type(file_name) is str:
            data = json.dumps(self.column)
            f = open(str(file_name)+".json", "w") 
            f.write(data)
            f.close()
            print("Table saved!")
        
    def loadTable(self, table_name):
        if type(table_name) is str:
            f = open(str(table_name)+".json", "r")
            data_string = f.read()
            
            self.column = json.loads(data_string)
        else:
            print("The path isn't a string.")   


#The Geometry class------------------------------------------------------------------------------------------------------------
class Geometry:
    def __init__(self):
        self.type = "geometry"
    
    def distance2D(self, x1, y1, x2, y2):
        x_d = (x2 - x1)**2
        y_d = (y2 - y1)**2
        
        d = math.sqrt(x_d + y_d)
        return "{:.6f}".format(d)
        
    def circleCircumference(self, radius):
        if (type(radius) is int) or (type(radius) is float):
            c = 2 * math.pi * radius
            return "{:.6f}".format(c)
        else:
            return None
       
    def circleArea(self, radius):
        if (type(radius) is int) or (type(radius) is float):
            a = math.pi * (radius**2)
            return "{:.6f}".format(a)
        else:
            return None
    
    def sphereArea(self, radius):
        if (type(radius) is int) or (type(radius) is float):
            A = 4 * math.pi * (radius ** 2)
            return "{:.6f}".format(A)
        else:
            return None
    
    def sphereVolume(self, radius):
        if (type(radius) is int) or (type(radius) is float):
            V = (4/3) * math.pi * (radius ** 3)
            return "{:.6f}".format(V)
        else:
            return None
    
    def coneArea(self, radius, height):
        if ((type(radius) is int) or (type(radius) is float)) and ((type(height) is int) or (type(height) is float)):
            A = (math.pi * radius * math.sqrt((radius**2)+(height**2))) + (math.pi * (radius**2))
            return "{:.6f}".format(A)
        else:
            return None
    
    def coneVolume(self, radius, height):
        if ((type(radius) is int) or (type(radius) is float)) and ((type(height) is int) or (type(height) is float)):
            V = (1/3) * math.pi * (radius ** 2) * height
            return "{:.6f}".format(V)
        else:
            return None