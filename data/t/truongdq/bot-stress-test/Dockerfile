FROM phusion/baseimage:0.9.18  
MAINTAINER Truong Do <do.q.truong> copyright Tito Garrido
<titogarrido@gmail.com>  
  
# Disable ssh.. we have docker exec  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-dev  
RUN pip install ws4py==0.3.2 tornado  
RUN pip install slackweb  
RUN apt-get install -y git  
RUN pip install git+https://github.com/truongdo/ipgetter.git  
ENV TERM dumb  
RUN echo "export TERM=xterm" >> /etc/bash.bashrc  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir -p /opt/src/  
ADD server.py /opt/src  
ADD tts_client.py /opt/src  
  
RUN mkdir /etc/service/test_bot  
ADD run /etc/service/test_bot/run  
RUN chmod 755 /etc/service/test_bot/run  
EXPOSE 16000  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

