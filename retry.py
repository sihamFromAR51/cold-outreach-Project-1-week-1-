business = [
    {"name":"arong", "chetagory":"cloting"},
    {"name":"blue", "chetagory":"clothing"},
    {"name":"bilashi", "chetagory":"design"}

    ]

stru = (
    "hello! Sir its me Ador, i'm a professional ad expert for businesses \n"
    "i saw a big gap in your advertison sector, your {name} needs work\n"
    "as in you {chetagory} we need to relay havily on AD's but you guys dont even try to get proper ads\n"
    "i can plan and help you to do tha if you give me a chance\n"
    "your future ceo\n"
    "Ador"
)


for busi in business:
    messege = stru.format(name = busi["name"], chetagory = busi["chetagory"])
    print("____")
    print(messege)