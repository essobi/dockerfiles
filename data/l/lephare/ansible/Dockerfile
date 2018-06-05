FROM williamyeh/ansible:alpine3  
  
RUN apk update \  
&& apk add postgresql git  
  
RUN adduser -u 1000 -D ansible  
USER ansible  
WORKDIR /app  
  
COPY ./roles.yml /tmp/roles.yml  
  
RUN ansible-galaxy install -r /tmp/roles.yml  
  
ENV ANSIBLE_PIPELINING=true  
ENV ANSIBLE_PERSISTENT_CONTROL_PATH_DIR=/tmp/ansible-ssh-%%h-%%p-%%r  
ENV ANSIBLE_RETRY_FILES_ENABLED=false  

