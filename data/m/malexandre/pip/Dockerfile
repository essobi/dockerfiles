FROM alpine  
LABEL maintainer "marc@malexandre.fr"  
  
RUN apk update  
RUN apk add git  
RUN apk add python  
RUN apk add py-pip  
RUN apk add py-pillow  
RUN apk add openssh-client  
RUN apk add openssl-dev  
RUN apk add python-dev  
RUN apk add libffi-dev  
RUN apk add build-base  
RUN apk add jpeg-dev  
RUN apk add zlib-dev  
RUN rm -rf /var/cache/apk/*  
RUN pip install --upgrade pip  
  
WORKDIR /code  

