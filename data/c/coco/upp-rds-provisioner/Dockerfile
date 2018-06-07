FROM alpine:3.5  
WORKDIR /data  
  
COPY requirements.txt /data/requirements.txt  
  
RUN apk add --no-cache python bind-tools bash openssl openssh ca-certificates
py-pip && \  
update-ca-certificates && \  
apk add --no-cache --virtual .build-dependencies python-dev build-base libffi-
dev openssl-dev git && \  
pip --no-cache-dir install -I -r /data/requirements.txt && \  
apk del .build-dependencies  
  
COPY cloudformation /data/cloudformation  
  
COPY inventory /data/inventory  
  
COPY ansible.cfg /data/  
  
COPY *.yml /data/  
  
COPY files /data/files  
  
COPY tasks /data/tasks  
  
COPY sh/* /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/*.sh  
  
CMD ["provision.sh"]

