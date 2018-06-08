FROM alpine:latest  
MAINTAINER pasi@lammi.eu  
  
RUN apk add --update py-pip curl py-jinja2 git  
RUN mkdir -p /app /app/data  
WORKDIR /app  
RUN git clone https://github.com/dtcooper/python-fitparse.git  
RUN pip install web.py  
  
RUN mv python-fitparse/fitparse /app  
RUN rm -rf webpy python-fitparse  
ADD web /app  
  
ENTRYPOINT ["/usr/bin/python", "ui.py"]  
EXPOSE 8080  
VOLUME ["/app/data"]  
  

