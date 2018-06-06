FROM debian:8  
MAINTAINER Alessandro Mereu <a.mereu@criticalcase.com>  
MAINTAINER Andrea Sosso <a.sosso@criticalcase.com>  
  
RUN apt-get -y update && apt-get -y install curl \  
&& apt-key adv --fetch-keys http://repo.powerdns.com/CBC8B383-pub.asc \  
&& echo 'deb [arch=amd64] http://repo.powerdns.com/debian jessie-metronome-
master main ' > /etc/apt/sources.list.d/pdns.list \  
&& echo 'Package: * ' >> /etc/apt/preferences.d/metronome \  
&& echo 'Pin: origin repo.powerdns.com' >> /etc/apt/preferences.d/metronome \  
&& echo 'Pin-Priority: 600' >> /etc/apt/preferences.d/metronome \  
&& curl https://repo.powerdns.com/CBC8B383-pub.asc | apt-key add - \  
&& apt-get -y update \  
&& apt-get -y install metronome \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Webserver  
EXPOSE 8000  
# Carbon Server  
EXPOSE 2003  
# Stats Data  
VOLUME /usr/share/metronome/stats  
  
# HTML files for UI  
VOLUME /usr/share/metronome/html  
  
CMD ["/usr/bin/metronome", "--stats-directory=/usr/share/metronome/stats", "--
daemon=0"]  
  
# Metadata params  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
# Metadata  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/criticalcase/metronome-docker" \  
org.label-schema.version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.url="https://www.criticalcase.com" \  
com.microscaling.license="MIT"  

