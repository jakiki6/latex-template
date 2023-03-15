all: main.pdf

view: main.pdf
	atril $<

main.pdf: main.tex
	pdflatex $<
	zip -l main.zip main.tex images/* Makefile
	pdfzip -p main.pdf -z main.zip main.pdf
	rm main.zip

clean:
	rm -f *.log *.aux *.pdf *.zip

.PHONY: all view clean
