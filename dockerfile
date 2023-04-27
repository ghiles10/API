FROM python:3.9-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install pytest
CMD ["pytest", "-v"]
