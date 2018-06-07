FROM factual/docker-cdh5-dev  
  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
ADD sshd_config /etc/ssh/  
  
RUN mkdir -p /share  
RUN mkdir -p /local  
  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" >>
/etc/apt/sources.list.d/docker.list  
  
RUN apt-get update && apt-get install -y byobu docker-engine python3-pip bash-
completion s3cmd awscli  
  
RUN mkdir -p /etc/service/docker  
ADD docker.sh /etc/service/docker/run  
  
# Jeff additions:  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y jq  
RUN apt-get install -y python-pip  
RUN pip install --upgrade pip  
  
#cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/home","/share", "/local"]  
  
# Jeff's additions:  
RUN /home/jpicard/code/predict/predict-py/init.sh  

