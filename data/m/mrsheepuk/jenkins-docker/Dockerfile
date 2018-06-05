FROM jenkins:latest  
COPY plugins.txt /plugins.txt  
RUN /usr/local/bin/plugins.sh /plugins.txt  
  
USER root  
  
# Change the jenkins GID / UID because 1000 is just stupid.  
RUN usermod -u 1100 jenkins && groupmod -g 1100 jenkins  
RUN find / -not \\( -path /sys/fs -prune \\) -not \\( -path /proc -prune \\)
-user 1000 -exec chown -h 1100 {} \; && find / -not \\( -path /sys/fs -prune
\\) -not \\( -path /proc -prune \\) -group 1000 -exec chgrp -h 1100 {} \;  
RUN usermod -g 1100 jenkins  
  
RUN curl -sSL https://get.docker.com/ | sh  
RUN usermod -aG docker jenkins  
USER jenkins  

