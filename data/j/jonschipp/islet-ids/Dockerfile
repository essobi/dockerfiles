# Snort and Suricata  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Jon Schipp <jonschipp@gmail.com>  
  
# Specify container username e.g. training, demo  
ENV VIRTUSER demo  
  
RUN apt-get update -qq  
RUN apt-get install -y snort suricata  
RUN apt-get install -y git vim emacs nano tcpdump gawk rsyslog  
RUN apt-get install -y --no-install-recommends man-db  
RUN mv /etc/suricata/suricata-debian.yaml /etc/suricata/suricata.yaml  
RUN chmod -R 777 /etc/snort /etc/suricata  
RUN adduser --disabled-password --gecos "" $VIRTUSER  
RUN echo "PATH=$PATH:/usr/sbin/:/usr/bin/" > /etc/profile.d/ids.sh && chmod
555 /etc/profile.d/ids.sh  
RUN echo "export TMOUT=1800; readonly TMOUT" > /etc/profile.d/timeout.sh &&
chmod 555 /etc/profile.d/timeout.sh  
RUN echo "alias snort='/usr/sbin/snort'" >> /etc/profile.d/ids.sh  
RUN echo "alias suricata='/usr/bin/suricata'" >> /etc/profile.d/ids.sh  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/snort  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/bin/suricata  

