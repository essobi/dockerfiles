FROM ubuntu:trusty  
  
# bypass postfix install prompt  
ENV DEBIAN_FRONTEND noninteractive  
  
# install and cleanup  
RUN apt-get update \  
&& apt-get install -y supervisor dovecot-common postfix nginx nginx-extras\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add and run install script  
COPY install.sh /install.sh  
RUN /install.sh \  
&& rm /install.sh  
  
RUN useradd -u 1000 -M docker  
  
CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  
VOLUME /mail  
EXPOSE 25 80

