FROM python:2.7.11-alpine  
  
RUN apk add --update-cache bash build-base zlib zlib-dev jpeg jpeg-dev libpng
libpng-dev freetype freetype-dev  
  
# To fix following error: IOError: decoder zip not available  
RUN ln -s /lib/libz.so /usr/lib/  
  
RUN pip install --upgrade pip && pip install pillow==2.6.1  
  
ADD . .  
  
ENTRYPOINT python ./images.py  
  
EXPOSE 4655  

