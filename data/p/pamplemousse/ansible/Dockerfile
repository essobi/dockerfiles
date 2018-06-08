FROM python:alpine  
  
RUN apk --update add \  
py-yaml py-jinja2 py-paramiko py-six py-setuptools git py-pip perl py-
simplejson rsync \  
&& apk add py-httplib2 py-netifaces py-msgpack openssh py-cryptography \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
\  
&& rm -rf /var/cache/apk/*  
  
ENV PATH /opt/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin  
ENV PYTHONPATH /opt/ansible/lib  
ENV ANSIBLE_LIBRARY /opt/ansible/library  
  
RUN apk --update add bash  
  
RUN adduser -u 1000 -D ansible  
USER ansible  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

