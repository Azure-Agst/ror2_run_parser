ifeq ($(OS),Windows_NT)
	py := python
else
	py := python3
endif

test:
	$(py) -m unittest -v tests

.PHONY: test