FROM phusion/baseimage:0.9.15  
MAINTAINER Malte Zacharias  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
lighttpd \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
supervisor \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
postfix \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
mailman  
  
ADD assets/install.sh /opt/install.sh  
  
RUN mkdir -p /etc/my_init.d  
ADD assets/install.sh /etc/my_init.d/setup_container.sh  
  
# SSH Key  
ADD assets/sshkey.pub /tmp/sshkey.pub  
RUN cat /tmp/sshkey.pub >> /root/.ssh/authorized_keys && rm -f /tmp/sshkey.pub  
  
# Lighttpd configuration  
ADD assets/lighttpd.conf /etc/lighttpd/lighttpd.conf  
  
# Start setup script and then processes  
CMD ["/sbin/my_init"]  
#CMD /opt/install.sh && /opt/run.sh  
# Clean-up apt  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare for first start  
RUN touch /tmp/firststart  
  
EXPOSE 25 80 22  
# Expose mailman archives for backup  
VOLUME /var/lib/mailman  

