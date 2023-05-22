Ticket_generator is a personal project to make tickets for a concert.
It was written due to the high volume of tickets and the different
sources of the elements used in the ticket.

The process followed is:
    1. Gather the QR codes from our source
    2. Write a text ID code of the ticket in Power Point.
       This text is going to be printed below the QR code.
    3. Run saving_code module from powerpoint_utilities.py
       This save each text ID code in the /texts folder.
    4. Run ticket_merge_gen.py to make individual tickets with
       the specific information of each one, and save them in
       the /individual_tickets folder
       There's a variable called four_code. This is a 4-code
       that properly identifies our event.
    5. Run pdf_print_generator.py to make sets of 4 tickets each.
    6. Run the make_sheet module from powerpoint_utilities.py
       in PowerPoint, so it makes new slides and paste the 
       previously generated sets; one set per slide.

This allowed us to make a pdf file of all the tickets ready to print!

    