FROM frolvlad/alpine-python2  
EXPOSE 80  
WORKDIR /code  
ADD . /code  
RUN touch index.html  
RUN apk --update add py-netifaces --update-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/  
CMD python index.py  
  

