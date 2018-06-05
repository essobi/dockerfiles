FROM python:2.7-alpine  
  
WORKDIR /hydrus/  
  
RUN apk add --update build-base libjpeg-turbo jpeg-dev linux-headers zlib-dev
libffi libffi-dev openssl-dev \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip install pyyaml beautifulsoup4 lz4 psutil Send2Trash twisted hsaudiotag
PyPDF2 Pillow numpy pycrypto PyOpenSSL service_identity \  
&& apk del build-base jpeg-dev linux-headers zlib-dev libffi-dev openssl-dev \  
&& rm -rf ~/.cache  
  
COPY ./ /hydrus/  
  
VOLUME /hydrus/db/  
  
EXPOSE 45870  
CMD ["python2", "server.py"]  

