FROM ubuntu:16.04  
# Set envs  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV MMS_VERSION latest  
  
RUN apt-get -qqy update \  
&& apt-get -qqy upgrade \  
&& apt-get -qqy install curl \  
&& apt-get -qqy install logrotate \  
&& apt-get -qqy install supervisor \  
&& apt-get -qqy install munin-node \  
&& apt-get -qqy install libsasl2-2 \  
&& curl -sSL https://cloud.mongodb.com/download/agent/monitoring/mongodb-mms-
monitoring-agent_${MMS_VERSION}_amd64.ubuntu1604.deb -o mms.deb \  
&& dpkg -i mms.deb \  
&& rm mms.deb \  
&& apt-get -qqy autoremove \  
&& apt-get -qqy clean \  
&& rm -rf /var/lib/apt/*  
  
# Add munin-node conf  
ADD munin/munin-node.conf /etc/munin/munin-node.conf  
  
# Add supervisord conf  
ADD supervisor /etc/supervisor  
  
# Add entrypoint  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

