FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
ENV DOCKER_CONTAINER 1  
RUN apt-get update  
RUN apt-get -y install gettext  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV WEBAPP_DIR=/code/  
ADD requirements.txt $WEBAPP_DIR  
WORKDIR $WEBAPP_DIR  
  
RUN pip install -r requirements.txt

