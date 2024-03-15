all: main.pdf

view: main.pdf
	atril $<

main.pdf: main.tex
	pdflatex $<
	# bibtex $(<:.tex=)
	pdflatex $<
	# pdflatex $<
	zip -l main.zip main.tex refs.bib gerplain.bst images/* code/* Makefile
	pdfzip -p main.pdf -z main.zip main.pdf
	rm main.zip

clean:
	rm -f *.log *.aux *.bbl *.blg *.toc *.pdf *.zip *.out

.PHONY: all view clean
