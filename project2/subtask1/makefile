.DEFAULT_GOAL := run

requirements: requirements.txt
	@pip install -r requirements.txt
	@echo "All requirements downloaded!"

run: main.py
	@python3 main.py

clean:
	