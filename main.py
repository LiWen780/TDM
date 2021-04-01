import os
import TDM

tb = TDM.Table()

tb.addColumn("America")
tb.addColumn("Africa")
tb.addColumn("Asia")
tb.addColumn("Oceania")
tb.addColumn("Europe")

tb.addRow("America", ["Brazil","Mexico", "USA", "Canada","Haiti","Costa Rica","Panama","Colombia"])
tb.addRow("Asia", ["China","Japan", "Thailand", "South Korea","Indonesia","Vietnam","India"])
tb.addRow("Africa", ["Egypt","South Africa", "Morocco", "Nigeria","Congo", "Niger","Angola","Tunisia","Syria"])
tb.addRow("Oceania", ["Australia","New Zealand", "Papua New Guinea", "Fiji","Samoa","Solomon islands"])
tb.addRow("Europe", ["United Kingdom","Russia", "Sweden", "France","Italy","Germany","Spain"])

tb.display()

os.system("pause")