FROM phusion/baseimage:0.9.19  
LABEL MAINTAINER Eric Weissgerber <eweissge@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Speed up APT  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# See https://help.ubuntu.com/community/DansGuardian  
RUN set -x \  
&& apt-get update -q \  
&& apt-get install -qy dansguardian squid \  
&& apt-get install -qy clamav \  
&& freshclam  
  
RUN set -x \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Doesn't seem to work, permissions were set manually on the host  
# in /var/lib/docker/volumes  
# RUN chown -R proxy:proxy /var/spool/squid  
COPY dansguardian.conf /etc/dansguardian/dansguardian.conf  
COPY template.html /etc/dansguardian/languages/ukenglish/template.html  
COPY dansguardianf1.conf /etc/dansguardian/dansguardianf1.conf  
COPY squid.conf /etc/squid/squid.conf  
#RUN echo 'always_direct allow all' >> /etc/squid/squid.conf  
# Create dir to keep things tidy  
RUN mkdir /files  
  
VOLUME /var/spool/squid  
  
COPY entrypoint.sh /files/entrypoint.sh  
  
EXPOSE 8080/tcp  
  
ENTRYPOINT ["/files/entrypoint.sh"]  

