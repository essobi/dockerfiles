# docker build --rm -t ansible-alpine3 .  
FROM 1science/alpine  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run ansible roles and playbooks"  
  
RUN apk --update add sudo ansible git py-pip \  
&& mkdir -p /etc/ansible \  
&& echo "localhost ansible_connection=local" > /etc/ansible/hosts  
  
CMD ["/bin/bash"]  
  

