install:
	python -m pip install rasa fastapi uvicorn

init: install
	rasa init