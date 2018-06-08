FROM python:3.5  
MAINTAINER Elliot Nunn <elliotnunn@fastmail.com>  
  
COPY lzss.c /  
RUN gcc -O3 -Wall -std=c11 -o /usr/local/bin/lzss lzss.c && rm lzss.c  
  
COPY *make *dump /usr/local/bin/  
COPY *.py /usr/local/lib/python/  
  
ENV PYTHONPATH /usr/local/lib/python:$PYTHONPATH  

