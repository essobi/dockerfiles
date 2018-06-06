FROM ubuntu:16.04  
LABEL maintainer "Seiya Nuta <nuta@seiya.me>"  
  
RUN apt-get update && apt-get install -qy clang python3 build-essential git  
RUN useradd -u 9000 -r -s /bin/false app  
  
USER app  
COPY . /usr/src/app  
VOLUME /code  
WORKDIR /code  
  
CMD ["/usr/src/app/run.py"]  

