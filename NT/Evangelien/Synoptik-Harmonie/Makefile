all: mt.pdf mk.pdf lk.pdf

mt.pdf: mt.dot
	dot $< -Tpdf -o $@

mt.dot: mt.py events.py
	python mt.py

mk.pdf: mk.dot
	dot $< -Tpdf -o $@

mk.dot: mk.py events.py
	python mk.py

lk.pdf: lk.dot
	dot $< -Tpdf -o $@

lk.dot: lk.py events.py
	python lk.py
