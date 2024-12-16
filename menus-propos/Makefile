all: index.html

index.html: menus_propos.md head.html foot.html
	python -m markdown -x footnotes2 menus_propos.md -f output.html
	cat head.html output.html foot.html > _tmp.html
	rm output.html
	mv _tmp.html index.html

clean:
	rm -f _tmp.html index.html output.html
