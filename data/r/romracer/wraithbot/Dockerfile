FROM phusion/baseimage:0.9.19  
MAINTAINER romracer <romracer@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables.  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# set sane localeRUN locale-gen en_US en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Correct user and group uid/guid  
RUN usermod -u 1100 nobody && \  
usermod -g 100 nobody && \  
usermod -d /config nobody  
  
# update base image  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
# dependicies of wraith-bot  
RUN apt-get -y --no-install-recommends install libssl1.0.0:i386 libc6-i386
libgcc1:i386 aiccu oidentd  
  
# download latest maint release  
RUN mkdir -p /opt/wraith  
COPY wraith.Linux-v1.4.8-9-g2424dd8d.tar.gz /opt/wraith/wraith.Linux-
maint.tar.gz  
RUN tar -xzf /opt/wraith/wraith.Linux-maint.tar.gz -C /opt/wraith && \  
rm -f /opt/wraith/wraith.Linux-maint.tar.gz && \  
mv /opt/wraith/wraith.Linux-* /opt/wraith/wraith  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# run as nobody instead of root & fix permissions  
RUN chown -R nobody:users /opt/wraith && chmod 700 /opt/wraith/wraith  
RUN cp -a /etc/aiccu.conf /etc/aiccu.conf.orig  
  
VOLUME ["/config"]  
  
# Add config.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD config.sh /etc/my_init.d/config.sh  
RUN chmod +x /etc/my_init.d/config.sh  
  
# Add wraith bots to runit  
RUN mkdir -p /etc/service/oidentd  
ADD start-oidentd.sh /etc/service/oidentd/run  
RUN chmod +x /etc/service/oidentd/run  
  
# Add aiccu tunnel to runit  
#RUN mkdir -p /etc/service/aiccu  
#ADD start-aiccu.sh /etc/service/aiccu/run  
#RUN echo '#!/bin/bash\n\nexec /sbin/setuser nobody sleep inf' >
/etc/service/aiccu/finish  
#RUN chmod +x /etc/service/aiccu/run && chmod +x /etc/service/aiccu/finish  
# Add wraith bots to runit  
RUN mkdir -p /etc/service/wraith-bot  
ADD wraith-bot.sh /etc/service/wraith-bot/run  
RUN echo '#!/bin/bash\n\nexec /sbin/setuser nobody sleep inf' >
/etc/service/wraith-bot/finish  
RUN chmod +x /etc/service/wraith-bot/run && chmod +x /etc/service/wraith-
bot/finish  
  
# Add wraith hub to runit  
RUN mkdir -p /etc/service/wraith-hub  
ADD wraith-hub.sh /etc/service/wraith-hub/run  
RUN echo '#!/bin/bash\n\nexec /sbin/setuser nobody sleep inf' >
/etc/service/wraith-hub/finish  
RUN chmod +x /etc/service/wraith-hub/run && chmod +x /etc/service/wraith-
hub/finish  

