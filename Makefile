FIGURES=Plot1.png Plot2.png

top500Domains.csv:
	wget -O top500Domains.csv 'https://moz.com/top-500/download/?table=top500Domains'

Plot1.png Plot2.png: web_publish_date.py top500Domains.csv
	python web_publish_date.py

report.pdf: report.tex $(FIGURES)
	latexmk -pdf

.PHONY: 
	clean almost_clean

clean: almost_clean
	rm -f $(FIGURES)
	
almost_clean:
	latexmk -c
	rm -rf __pycache__
	rm -f top500Domains.csv