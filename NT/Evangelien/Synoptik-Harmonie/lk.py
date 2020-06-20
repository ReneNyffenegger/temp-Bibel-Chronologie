import events

dot = events.startDot('lk')

dot.writeEvents()

dot.edge('Kommt_in_Vaterstadt'              , 'Schwiegermutter_Petri_Fieberkrank')
dot.edge('Schwiegermutter_Petri_Fieberkrank', 'Heilung_Aussaetziger')

dot.end()
