FROM alpine  
  
LABEL maintainer "Viktor Adam <rycus86@gmail.com>"  
  
RUN apk add --no-cache python py2-pip git ca-certificates  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
RUN adduser -S webapp  
USER webapp  
  
ADD src /app  
WORKDIR /app  
  
STOPSIGNAL SIGINT  
  
CMD [ "python", "app.py" ]  

