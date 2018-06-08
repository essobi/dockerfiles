FROM python:2.7-alpine  
  
MAINTAINER giuem <i@giuem.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
RUN apk --no-cache add autoconf g++ ca-certificates && \  
pip install --no-cache-dir -r requirements.txt && \  
apk del g++ autoconf && \  
rm .git -rf  
  
ENV PORT 80  
EXPOSE $PORT/tcp  
  
VOLUME ["/usr/src/app/"]  
  
CMD ["python","/usr/src/app/run.py"]  

