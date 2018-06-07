FROM illallangi/apache:latest  
  
COPY ansible/* /etc/ansible.d/php/  
RUN /usr/local/bin/ansible-runner.sh php

