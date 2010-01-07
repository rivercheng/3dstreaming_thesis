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

$(FILENAME).aux: $(FILENAME).tex $(FIGURES) abstract.tex mesh.tex dstream.tex p2p.tex mm09-3dstreaming.tex intro.tex survey.tex conclusion.tex
	latex $(FILENAME).tex

$(FILENAME).bbl:	$(FILENAME).bib
	bibtex $(FILENAME)

clean:
	rm *.log *.blg *.bbl *.aux *.ps *.dvi $(FILENAME).pdf
