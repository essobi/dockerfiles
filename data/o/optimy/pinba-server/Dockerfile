FROM tony2001/pinba  
MAINTAINER mgillot@optimy.com  
  
# add utility packages  
RUN apt-get update && apt-get install -y tcpdump mysql-client libdbi1 libdbd-
mysql collectd python git curl  
  
# setup pinba exec  
RUN echo '#!/bin/bash\nmysql -u root -h 127.0.0.1 -D pinba' > /usr/bin/pinba  
RUN chmod a+x /usr/bin/pinba  
  
# add optimy custom schema to pinba database  
COPY tmp/* /tmp/  
  
RUN touch /var/log/collectd.log  
# Make directory for plugin and clone it there  
RUN cd ~ &&\  
mkdir AWSPlugin  
RUN cd ~/AWSPlugin &&\  
git clone https://github.com/awslabs/collectd-cloudwatch.git  
# Copy file to automate plugin installation and run it  
COPY file /root/AWSPlugin/collectd-cloudwatch/src/file  
RUN cd /root/AWSPlugin/collectd-cloudwatch/src/ &&\  
./file  
# Copy our configs so everything works as expected  
COPY collectd.conf /etc/collectd/collectd.conf  
COPY plugin.conf /opt/collectd-plugins/cloudwatch/config/plugin.conf  
COPY whitelist.conf /opt/collectd-plugins/cloudwatch/config/whitelist.conf  
COPY credentials /root/.aws/credentials  
COPY filters.conf /etc/collecd/collecd.conf.d/filters.conf  
  
ENTRYPOINT ["/tmp/entrypoint.sh"]  

