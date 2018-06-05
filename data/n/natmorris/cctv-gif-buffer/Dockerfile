FROM alpine:3.5  
MAINTAINER Nat Morris <nat@nuqe.net>  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
jpeg-dev \  
zlib-dev \  
&& pip install virtualenv  
  
ENV LIBRARY_PATH=/lib:/usr/lib  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
# Copy requirements before app so we can cache PIP dependencies on their own  
RUN mkdir /app  
COPY requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt  
  
COPY buffer.py /app/  
COPY cctvgifbuffer/*.py /app/cctvgifbuffer/  
  
RUN rm -rf \  
/root/.cache \  
/tmp/*  
RUN rm -rf /var/cache/apk/*  
  
EXPOSE 8080/tcp  
  
CMD ["/env/bin/python", "/app/buffer.py", "-c /config/config.yaml"]  

