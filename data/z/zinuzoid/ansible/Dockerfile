FROM alpine:edge  
MAINTAINER Jetsada Machom <jim@imjim.im>  
RUN apk --no-cache add \  
py-yaml \  
py-jinja2 \  
py-paramiko \  
py-setuptools \  
git \  
py2-pip \  
perl \  
py-simplejson \  
rsync \  
py-httplib2 openssh && \  
apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /etc/ansible/  
RUN echo "[local]" > /etc/ansible/hosts && \  
echo "localhost ansible_connection=local" >> /etc/ansible/hosts  
RUN mkdir -p /opt/ansible/ansible  
WORKDIR /opt/ansible/ansible  
RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible && \  
git checkout v2.1.1.0-1 && \  
git submodule update --init  
  
ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/ansible/lib  
ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library  
  
RUN mkdir /ansible  
WORKDIR /ansible  
  

