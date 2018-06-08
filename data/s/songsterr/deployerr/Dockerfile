FROM alpine:3.5  
RUN apk add --no-cache python ansible curl openssh-client  
  
RUN mkdir /root/.ssh/ && echo -e 'StrictHostKeyChecking no\n' >
/root/.ssh/config && chmod 0600 /root/.ssh/config && \  
touch /root/.ssh/id_songsterr_deploy && chmod 0600
/root/.ssh/id_songsterr_deploy && \  
mkdir /etc/ansible/ && echo -e "[defaults]\nhost_key_checking =
False\ncallback_whitelist = profile_tasks\n" > /etc/ansible/ansible.cfg &&
chmod 0600 /etc/ansible/ansible.cfg  
  
ADD script.sh /bin/  
RUN chmod +x /bin/script.sh  
ENTRYPOINT /bin/script.sh  

