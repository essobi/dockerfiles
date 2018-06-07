FROM python:3.6.4-alpine  
  
MAINTAINER Erignoux Laurent <lerignoux@gmail.com>  
  
RUN apk update && apk add zlib-dev jpeg-dev postgresql-libs && \  
apk add --virtual .build-deps build-base python3-dev musl-dev postgresql-dev  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD ./requirements.txt /app/  
RUN pip install -r requirements.txt  
  
RUN apk --purge del .build-deps  
  
CMD ["python", "manage.py", "runserver", "0:8000"]  

