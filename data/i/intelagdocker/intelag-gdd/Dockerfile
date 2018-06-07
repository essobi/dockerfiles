# Dockerfile for growing degree days  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --update add --no-cache \  
lapack-dev \  
gcc \  
freetype-dev  
  
RUN apk add python py-pip python-dev  
  
# Install dependencies  
RUN apk add --no-cache --virtual .build-deps \  
gfortran \  
musl-dev \  
g++  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip install numpy  
  
### Add source file(s)  
ADD gdd.py /action/gdd.py  
RUN rm /action/exec  
ADD exec /action/  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

