import events

dot = events.startDot('mk')

dot.writeEvents()

dot.edge('Schwiegermutter_Petri_Fieberkrank', 'Heilung_Aussaetziger')
dot.edge('Heilung_Aussaetziger'             , 'Kommt_in_Vaterstadt')

dot.end()
