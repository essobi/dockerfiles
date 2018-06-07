FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
WORKDIR /code  
  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
  
COPY . /code/  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN apt-get update && apt-get install -y \  
netcat  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  

