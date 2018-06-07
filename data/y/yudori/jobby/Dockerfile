FROM ubuntu:16.04  
MAINTAINER Richard Oyudo <ebube.rc@gmail.com>  
  
COPY ./docker/web/backend/backend-entrypoint.sh /  
COPY ./docker/web/backend/worker-entrypoint.sh /  
COPY ./requirements /app/requirements  
  
WORKDIR /app  
  
# Install linux stuff  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Install backend stuff  
RUN add-apt-repository ppa:deadsnakes/ppa  
RUN apt-get update && apt-get install -y build-essential python3.6
python3.6-dev python3-pip git libhunspell-dev  
  
RUN python3.6 -m pip install pip==9.0.1  
RUN python3.6 -m pip install -r requirements/dev.txt  
RUN python3.6 -m spacy download en  

