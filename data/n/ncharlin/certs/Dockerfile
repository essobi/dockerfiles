FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y python python-pip netcat && rm -rf
/var/lib/apt/lists/*  
RUN mkdir /code  
WORKDIR /code  
COPY requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  
EXPOSE 8080  
ENTRYPOINT ["/code/docker-entrypoint.sh"]

