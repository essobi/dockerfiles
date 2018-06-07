FROM debian:wheezy  
MAINTAINER hello@neilellis.me  
ENV NEW_RELIC_LICENSE_KEY changeme  
LABEL Description="New Relic Linux Server Monitor" vendor="New Relic Inc."  
COPY daemon/nrsysmond.x64 /usr/sbin/nrsysmond  
COPY nrsysmond.cfg nrsysmond.cfg  
COPY run.sh run.sh  
RUN chmod 755 run.sh /usr/sbin/nrsysmond  
CMD ./run.sh  

