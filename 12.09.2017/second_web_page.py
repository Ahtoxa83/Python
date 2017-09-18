from bottle import run, route, response, request

def make_page(text):
    return """<!DOCTYPE HTML>
<html><head><title>My second page!</title>
<meta charset="utf-8">
</head>
<body style="background-color: rgb(237, 238, 240); color: rgb(0, 0, 0);"
 alink="#ee0000" link="#0000ee" vlink="#551a8b">
<div style="font-family: Verdana; "text-align: left; margin-left: 40px;">
<h1><div style="text-align: center; text-decoration: underline;">Игра "21 палочка"</div></h1>
    {}
</div>
</body>
</html>""".format(text)

@route("/")
def main_view():
    return make_page("""<h2><div style="text-align: center;">
    Правила игры</div></h2>
    
    На столе находится 21 палочка. Ходы делаются игроками по очереди. За один
    ход игрок берёт себе со стола одну, две или три палочки. Игрок, который
    возьмёт последнюю палочку со стола, проигрывает. Пропускать ход нельзя.

    <p style="font-style: italic;"><a href="/start/">Начать игру!</a></p>""")

@route("/start/")
def start_view():
    response.set_cookie("sticks", "21", path="/take")
    takes = range (1, 4)
    template = "<td><a href=\"/take/{n}/\">Беру {n}</a></td>"
    takes_list = [template.format(n=your_turn) for your_turn in takes]
    return make_page("""<h2><div style="text-align: center;">Игра начата!</div></h2>
        На столе 21 палочка. Сколько возьмёте? <br/>
        <p><td style="font-family: Verdana;">""" + "\n".join(takes_list) + """</td></p>""")
        

@route("/take/<your_turn:re:[1-3]>/")
def take_n_view(your_turn):
    response.set_cookie("sticks", "21", path="/take")
    sticks = int(request.cookies.get("sticks"))
    left_your_turn = sticks - int(your_turn)
    my_turn = 4 - int(your_turn)
    left_my_turn = left_your_turn - my_turn
    takes = range (1, 4)
    template = "<td><a href=\"/take/{n}/\">Беру {n}</a></td>"
    takes_list = [template.format(n=your_turn) for your_turn in takes]
        
    if left_my_turn == 1:
        return make_page("Вы проиграли! Осталась " + str(left_my_turn) + " палочка."
            + """<br/> <p style="font-style: italic;"><a href="/start/">Начать сначала!</a></p>""")
    elif sticks < 1 or sticks > 21:
        return make_page("""<p style="font-family: Verdana;>Читер не пройдёт!</p>""" + """<br/> <p style="font-style: italic;"><a href="/start/">Начать сначала!</a></p>""")
    else:
        response.set_cookie("sticks", str(left_my_turn), path="/take")
        
    return make_page('''   
            Было палочек: {n} <br />
            <p></p>
            Вы взяли: {your_turn}, осталось: {left_your_turn} <br />
            <p></p>
            Я беру: {my_turn} <br />
            <p></p>
            Осталось палочек: {left_my_turn} <br />
            <p></p><p></p>
            '''.format(n=sticks, left_your_turn = left_your_turn,
        left_my_turn = left_my_turn, my_turn = my_turn, your_turn = your_turn) +
    "\n".join(takes_list) + 
    """<p style="font-style: italic;"><br/>
    <a href="/start/">Начать сначала!</a></p>""")
    
run()
