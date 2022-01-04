up:
	uvicorn main:app --reload

test:
	python3 -m pytest test.py -v
