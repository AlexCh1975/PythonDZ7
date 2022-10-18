# Модуль экспорт в html

p = []

def init(data):
    global p
    p = data
   

def rendere_html():
   style = 'style = "from size:22px;"'
   html = '<html>\n <head></head>\n <body>\n'
   for i in p:
    html += '   <p>{}</p>\n'.format(i)
   html += ' </body>\n</html>'

   with open('index.html', 'w', encoding='utf-8') as page:
    page.write(html)

