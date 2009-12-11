.SUFFIXES: .ps .jpg
FILENAME=thesis
BIBS=mesh.bbl $(FILENAME).bbl

all:	$(FILENAME).ps 
	ps2pdf $(FILENAME).ps

$(FILENAME).ps:	$(FILENAME).dvi
	dvips -P cmz -t letter -o $(FILENAME).ps $(FILENAME).dvi

$(FILENAME).dvi:	$(FILENAME).tex $(FILENAME).aux $(FILENAME).bbl $(FIGURES) 
	latex $(FILENAME).tex
	latex $(FILENAME).tex

$(FILENAME).pdf:	$(FILENAME).tex $(FILENAME).aux $(BIBS)
	pdflatex $(FILENAME).tex
	pdflatex $(FILENAME).tex

$(FILENAME).aux: $(FILENAME).tex $(FIGURES) mesh.tex dstream.tex p2p.tex mm09-3dstreaming.tex intro_survey.tex
	latex $(FILENAME).tex

$(FILENAME).bbl:	$(FILENAME).bib
	bibtex $(FILENAME)

clean:
	rm *.log *.blg *.bbl *.aux *.ps *.dvi *.pdf
