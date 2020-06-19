import events

dot = events.startDot('mk')

dot.writeEvents()

dot.edge('Heilung_Aussaetziger', 'Schwiegermutter_Petri_Fieberkrank')

dot.end()
