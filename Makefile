all: main.pdf

view: main.pdf
	atril $<

main.pdf: main.tex
	pdflatex $<
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.log *.aux *.bbl *.blg *.toc *.pdf *.zip *.out

.PHONY: all view clean
