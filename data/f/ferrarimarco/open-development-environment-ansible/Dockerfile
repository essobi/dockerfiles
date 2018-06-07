FROM alpine:3.7  
LABEL maintainer "ferrari.marco@gmail.com"  
  
RUN apk add --update \  
build-base \  
git \  
libffi \  
libffi-dev \  
musl \  
openssh-client \  
openssl \  
openssl-dev \  
python \  
python-dev \  
sshpass \  
&& rm /var/cache/apk/*  
  
# install and update pip  
RUN python -m ensurepip \  
&& pip install --no-cache-dir --upgrade pip  
  
# install Ansible  
COPY requirements.txt requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  

