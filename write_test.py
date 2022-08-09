import pygsheets


#authorization
gc = pygsheets.authorize(service_file='./key/key.json')
sh = gc.open('test_sheet')
wks = sh[0]
current_row_count = len(wks.get_all_records()) + 1
cell_addr = "E"+str(current_row_count)
print(cell_addr)
value = wks.get_value(cell_addr)

if len(value)==0:
    wks.update_value(cell_addr, "test", parse=None)




