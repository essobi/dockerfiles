FROM hmmbug/tesseract:latest  
LABEL maintainer "mark@markhollow.com"  
  
RUN apk add --no-cache build-base gcc python python-dev git cython \  
cython-dev curl zlib zlib-dev jpeg-dev libpng-dev tiff-dev && \  
curl -o - https://bootstrap.pypa.io/get-pip.py | python && \  
pip install Pillow && \  
mkdir /build && \  
cd /build && \  
git clone https://github.com/sirfz/tesserocr.git && \  
cd tesserocr && \  
git checkout tesseract4 && \  
python setup.py install && \  
apk del cython-dev python-dev zlib-dev jpeg-dev libpng-dev tiff-dev  
RUN mkdir /test  
  
COPY test/* /test/  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-h"]  

