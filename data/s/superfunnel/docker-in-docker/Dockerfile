FROM docker:17.07  
RUN apk update  
RUN apk add --no-cache python3 py3-pip bash zip python3-dev gcc g++ && rm -rf
/var/cache/apk/*  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
RUN pip3 install bottle numpy cython pandas  
  
RUN pip3 install docker-compose awscli awscli-local redis boto3 idutils
msgpack-python pytz cerberus addict raven ciso8601  
  
RUN apk update && apk add libffi-dev openssl-dev  
RUN pip3 install moto[server]  
RUN ln -s /usr/bin/python3.6 /usr/bin/python  
RUN ln -s /usr/bin/pip3.6 /usr/bin/pip  
  

