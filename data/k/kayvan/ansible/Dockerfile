FROM iron/python:2-dev  
  
MAINTAINER Kayvan Sylvan <kayvansylvan@gmail.com>  
  
RUN apk add --no-cache g++ gcc make git python-dev \  
libffi-dev openssl-dev openssh-client sshpass  
RUN rm -rf /usr/share/man /tmp/* /var/cache/apk/* /root/.gnupg  
  
RUN pip install --upgrade pip  
RUN pip install ansible  

