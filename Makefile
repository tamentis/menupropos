all:
	@echo "Pick a target"

dist:
	rm -rf dist/
	mkdir -p dist
	cp index.html dist/
	# Menus Propos
	mkdir -p dist/menus-propos
	make -C menus-propos
	cp menus-propos/index.html dist/menus-propos

venv:
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf dist
	make -C menus-propos clean
