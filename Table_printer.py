def printTable(tableData):
    
    colWidths = [max(len(item) for item in col) for col in tableData]
    
    for row in zip(*tableData):
        print(" ".join(item.rjust(width) for item, width in zip(row, colWidths)))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
