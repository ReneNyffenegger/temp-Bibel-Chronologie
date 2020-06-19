class gospelDot:

    def __init__(self, abbr):

        self.f = open('{}.dot'.format(abbr), 'w')
        self.f.write('digraph {} {{\n'.format(abbr))
        
    def event(self, name, mt, mk, lk, text):
        self.f.write('''{} [ label = < <table> 
           <tr><td align="text" colspan="3">{}</td></tr>
           <tr><td>{}</td><td>{}</td><td>{}</td></tr>
           </table> > ]
        '''.format(name, text, mt, mk, lk))

    def writeEvents(self):
        self.event('Schwiegermutter_Petri_Fieberkrank', '8:14', '1:29', '4:38', 'Petri Schwiegermutter Fieberkrank')

    def end(self):
        self.f.write('\n}')

def startDot(abbr):
    dot = gospelDot(abbr)
    return dot
