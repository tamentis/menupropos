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

clean:
	rm -rf dist
