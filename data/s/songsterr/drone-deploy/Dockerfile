FROM alpine:3.7  
RUN apk add --no-cache python3 curl openssh-client alpine-sdk python3-dev
libffi-dev openssl-dev && pip3 install ansible && apk del alpine-sdk alpine-
sdk python3-dev libffi-dev openssl-dev  
  
RUN mkdir /root/.ssh/ && echo -e 'StrictHostKeyChecking no\n' >
/root/.ssh/config && chmod 0600 /root/.ssh/config && \  
touch /root/.ssh/id_songsterr_deploy && chmod 0600
/root/.ssh/id_songsterr_deploy && \  
mkdir /etc/ansible/ && echo -e "[defaults]\nhost_key_checking =
False\ncallback_whitelist = profile_tasks" > /etc/ansible/ansible.cfg && chmod
0600 /etc/ansible/ansible.cfg  
  
ADD script.sh /bin/  
ADD docker-gc-playbook.yml /etc/ansible/  
RUN chmod +x /bin/script.sh  
ENTRYPOINT /bin/script.sh  

