FROM alpine:3.3  
MAINTAINER John Jansen <john.jansen@me.com>  
  
RUN apk add --no-cache curl python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
RUN pip install --upgrade pip  
RUN pip install progressbar  
RUN pip install https://github.com/johnjansen/wp-download/zipball/master  
  
ADD wpdownloadrc.conf /root/.wpdownloadrc  
  
RUN mkdir /wikipedia  
VOLUME ["/wikipedia"]  
  
ENTRYPOINT ["wp-download", "--resume", "-v", "/wikipedia"]  

