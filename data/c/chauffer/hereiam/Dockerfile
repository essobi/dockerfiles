FROM python:3-alpine  
  
WORKDIR /app  
  
COPY requirements.txt /app/  
RUN apk add --no-cache --virtual=.run-deps libpq && \  
apk --no-cache --virtual=.build-deps add musl-dev build-base postgresql-dev &&
\  
pip install -r requirements.txt && \  
apk del .build-deps  
  
COPY . /app  
  
CMD ["python3", "app.py"]

