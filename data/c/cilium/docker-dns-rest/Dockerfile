FROM alpine:3.1  
MAINTAINER "André Martins <aanm90@gmail.com>"  
ENV PY=2.7.9-r0  
RUN apk add --update python=$PY python-dev=$PY gcc libgcc libc-dev py-pip
libev  
COPY ./requirements.txt /data/requirements.txt  
RUN pip install -r /data/requirements.txt  
RUN apk del python-dev gcc libgcc libc-dev py-pip libev  
RUN rm -rf /tmp/*  
RUN rm -rf /var/cache/apk/*  
EXPOSE 80  
COPY . /data  
ENTRYPOINT ["/data/docker_dnsrest"]  
  

