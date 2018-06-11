FROM alpine:3.5  
RUN apk update && \  
apk upgrade  
  
RUN apk add --update bash build-base py2-pip python-dev openssl-dev libffi-dev
&& rm -rf /var/cache/apk/*  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade requests[security] pyopenssl ndg-httpsclient pyasn1
virtualenv  
  
RUN virtualenv /app/build/env  
  
RUN source /app/build/env/bin/activate && pip install --upgrade flask zappa  
  
CMD ["/bin/bash"]  

