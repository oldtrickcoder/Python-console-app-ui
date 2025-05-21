import asciichartpy as acp

def AsciiChart():   
   data = [3, 8, 1, 9, 4]
   chart = acp.plot(data, {'height': 5})
   print(chart)