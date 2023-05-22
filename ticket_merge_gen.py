from PIL import Image

def charge_images(n,four_code):
    '''
    Methos to charge the elements that will form the whole ticket:
    The design of the ticket, its QR code, and the text code to print
    below the QR.

    Arguments:
        n:              The ticket number
        code:     The four letters code of the specific event
    '''
    ticket = Image.open("img/plain_ticket.png")
    qr = Image.open(f"QR/_MW-{four_code}-{n}_.png")
    event_code = Image.open(f"texts/{n}.png").convert("RGBA")
    return ticket,qr,event_code

def merge_ticket(ticket,qr,event_code):
    '''
    Merge the elements (ticket design, QR code and text code) by
    making a new image and placing each element in a proper location.

    Arguments:
        ticket:     Ticket design
        qr:         The qr object
        event_code: The text code
    '''
    qr = qr.resize((314,399),reducing_gap = 3)
    event_code = event_code.resize((306,92),reducing_gap = 3)
    ticket.paste(qr,(1626,136),qr)

    # # Dimensions calculated by hand
    # ticket.paste(event_code,(1629,456),event_code)
    # ticket.save("testold.png", format="png")
    
    # Dimensions calculated with proportions
    ticket.paste(event_code,(1626 + qr.width//2 - event_code.width//2,456),event_code)
    return ticket


four_code = 'ATEX'
for n in range(200):
    k = str(n+1).zfill(3)
    ticket,qr,event_code = charge_images(k,four_code)
    img = merge_ticket(ticket,qr,event_code)
    img.save(f"individual_tickets/ticket_{k}.png", format="png",resolution=100)