# This program converts a long flights string into
# a nicely formatted output
 
flights = ("_Delayed_Departure;fao93766109;txl2133758440;11:25"
"+_Arrival;bru0943384722;fao93766109;11:45"
"+_Delayed_Arrival;hel7439299980;fao93766109;12:05"
"+_Departure;fao93766109;lis2323639855;12:30")
 
# X Delayed Departure from FAO to TXL (11h25)
#             Arrival from BRU to FAO (11h45)
#   X Delayed Arrival from HEL to FAO (12h05)
#           Departure from FAO to LIS (12h30)

pflights = flights.split("+")

for flight in pflights:
    inf, frm, to, tm = flight.split(";")
    pInf = inf.replace("_", " ").lstrip()
    pFrm = frm[:3].upper()
    pTo = to[:3].upper()
    pTm = tm.replace(":", "h")

    # TERNARY OPERATOR VE F-STRİNG KULLANMADAN:
    start = ""
    if pInf.startswith("Delayed"):
        start = "X "

    output = start + pInf + " from " + pFrm + " to " + pTo + \
        " (" + pTm + ")"
    print(output)
