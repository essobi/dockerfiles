FROM phusion/baseimage:latest  
  
MAINTAINER roach@dopegoat.com  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get install --no-install-recommends -y apache2-utils git git-core
build-essential libssl-dev g++ sshfs libxml2-dev python2.7 python3 python  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
RUN git clone https://github.com/c9/core.git /cloud9  
  
RUN useradd -m -k /dev/null -u 99 -g 100 -d /home cloud9 && sh -c 'echo
"cloud9:`openssl rand -base64 32`" | chpasswd'  
RUN mkdir /workspace  
RUN chown -R 99.100 /home /cloud9 /workspace  
  
RUN mkdir /etc/service/cloud9  
RUN echo '#!/bin/sh' >/etc/service/cloud9/run  
RUN echo 'export NODE_ENV="production"' >>/etc/service/cloud9/run  
RUN echo 'export HOME=/home' >>/etc/service/cloud9/run  
RUN echo 'cd /cloud9' >>/etc/service/cloud9/run  
RUN echo 'exec chpst -u $(getent passwd 99 | cut -d: -f1) /usr/bin/node
/cloud9/server.js --listen 0.0.0.0 --port 8080 -w /workspace -a
$C9USER:$C9PASS --collab' >>/etc/service/cloud9/run  
RUN chmod +x /etc/service/cloud9/run  
  
RUN touch /etc/service/cron/down  
  
RUN mkdir -p /etc/my_init.d  
RUN echo '#!/bin/bash' >/etc/my_init.d/100-cloud9.sh  
RUN echo 'if [ -z ${C9USER+x} ]; then echo "C9USER not set"; else usermod -l
$C9USER $(getent passwd 99 | cut -d: -f1) ; fi' >>/etc/my_init.d/100-cloud9.sh  
RUN chmod +x /etc/my_init.d/100-cloud9.sh  
  
USER cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
RUN sed -i 's#127.0.0.1#0.0.0.0#' /cloud9/configs/standalone.js  
  
USER root  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8080  

