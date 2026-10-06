PORT ?= 8000

# Re-run every target inside the flake's dev shell unless we're already in one.
ifndef IN_NIX_SHELL
RUN := nix develop --command
endif

.PHONY: build preview clean

build:
	$(RUN) python build.py

preview: build
	@(sleep 1 && open http://localhost:$(PORT) 2>/dev/null || xdg-open http://localhost:$(PORT)) &
	$(RUN) python -m http.server $(PORT) -d _site

clean:
	rm -rf _site result
