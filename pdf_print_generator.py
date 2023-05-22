from PIL import Image

for ticket_num in range(0,200,4):
    '''
    Make png files with 4 tickets each. 
    This png files are going to be imported in PowerPoint later.
    '''
    tk_1 = Image.open("individual_tickets/ticket_" + str(ticket_num+1).zfill(3) + ".png")
    tk_2 = Image.open("individual_tickets/ticket_" + str(ticket_num+2).zfill(3) + ".png")
    tk_3 = Image.open("individual_tickets/ticket_" + str(ticket_num+3).zfill(3) + ".png")
    tk_4 = Image.open("individual_tickets/ticket_" + str(ticket_num+4).zfill(3) + ".png")
    images = [tk_1,tk_2,tk_3,tk_4]
    sheet = Image.new('RGB',(tk_1.width,tk_1.height*4+10))

    for k,img in enumerate(images):
        h_pos = 0+k*img.height+3*(k+1)
        sheet.paste(img,(0,h_pos))   

    pdf_path = f'print_sets/set_{ticket_num//4+1}.png'
    sheet.save(pdf_path, "png" ,resolution=100.0)