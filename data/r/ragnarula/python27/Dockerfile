  
#taken from https://hub.docker.com/r/frolvlad/alpine-python3/~/dockerfile/  
  
FROM alpine:3.4  
  
RUN apk add bash --update && \  
apk add \--no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
apk add ca-certificates && \  
rm -r /root/.cache  
  
CMD python

