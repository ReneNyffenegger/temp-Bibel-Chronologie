all: mt.pdf mk.pdf lk.pdf

mt.pdf: mt.dot
	dot $< -Tpdf -o $@

mt.dot: mt.in.dot events.dot
	cpp -P $< -o $@

mk.pdf: mk.dot
	dot $< -Tpdf -o $@

mk.dot: mk.in.dot events.dot
	cpp -P $< -o $@

lk.pdf: lk.dot
	dot $< -Tpdf -o $@

lk.dot: lk.in.dot events.dot
	cpp -P $< -o $@

clean:
	rm -f mt.dot mk.dot lk.dot *.pdf
