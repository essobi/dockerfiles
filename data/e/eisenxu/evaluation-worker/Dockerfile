FROM python:2.7-alpine  
  
WORKDIR /worker  
COPY requirements.txt /worker  
RUN pip install -r requirements.txt  
  
COPY main.py /worker  
COPY config.py /worker  
COPY worker /worker/worker  
  
RUN apk --update add curl git  
  
RUN curl http://downloads.drone.io/release/linux/amd64/drone.tar.gz | tar zx  
RUN install -t /bin drone  
  
ENTRYPOINT python main.py  

