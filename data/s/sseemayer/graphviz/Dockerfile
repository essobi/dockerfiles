FROM alpine:3.4  
RUN apk add --no-cache \  
graphviz python3 py-pip  
  
ADD requirements.txt ./  
RUN pip3 install -r requirements.txt  
  
ADD server.py ./  
CMD hug -f server.py  

