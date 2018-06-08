FROM php:7.1-alpine  
  
LABEL maintainer="Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>"  
  
ENV PYTHON_VERSION=2.7.14-r0  
ENV PY_PIP_VERSION=8.1.2-r0  
ENV SUPERVISOR_VERSION=3.3.3  
ENV QUEUE_CONNECTION=sqs  
ENV QUEUE_NAME=default  
  
# Install some dependenties  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev  
  
# Install pdo if you want to use database queue  
RUN docker-php-ext-install pdo pdo_mysql pcntl posix gd  
  
# Install supervisor  
RUN apk update && apk add -u python=$PYTHON_VERSION py-pip=$PY_PIP_VERSION  
RUN pip install supervisor==$SUPERVISOR_VERSION  
  
ADD supervisord.conf /etc/supervisord.conf  
  
# Copy scripts  
COPY start.sh /usr/local/bin/start.sh  
  
# Run supervisor  
CMD ["/usr/local/bin/start.sh"]

