FROM ubuntu:14.04  
ENV AWS_DEFAULT_REGION us-east-1  
RUN apt-get update -q  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip groff-base  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy sudo acl  
RUN sed -i -e '/^Defaults.*path/a\  
Defaults\t!requiretty' \  
-e 's/^%sudo.*ALL$/%sudo ALL=(ALL) NOPASSWD: ALL/' \  
-e '/^%sudo.*ALL$/a %wheel ALL=(ALL) NOPASSWD: ALL' /etc/sudoers  
RUN apt-get upgrade -y locales && locale-gen en_US.UTF-8 ; echo
LANG=en_US.UTF-8 | sudo tee /etc/default/locale  
RUN pip install awscli  
  
ENTRYPOINT ["/usr/local/bin/aws"]  

