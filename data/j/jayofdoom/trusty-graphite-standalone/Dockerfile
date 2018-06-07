FROM jayofdoom/docker-ubuntu-14.04  
MAINTAINER Jay Faulkner "jay.faulkner@rackspace.com"  
  
# Install required packages  
RUN apt-get update && \  
apt-get install -y build-essential git libcairo2 libcairo2-dev memcached \  
nodejs pkg-config python-cairo python-dev python-pip sqlite3 supervisor npm  
  
ADD src /tmp/src  
  
RUN pip install -r /tmp/src/requirements.txt  
  
# Copy configs into place and create needed dirs  
RUN cp -f /opt/graphite/conf/carbon.conf.example
/opt/graphite/conf/carbon.conf && \  
cp -f /opt/graphite/webapp/graphite/local_settings.py.example \  
/opt/graphite/webapp/graphite/local_settings.py && \  
cp -f /tmp/src/*.conf /opt/graphite/conf/ && \  
mkdir -p /opt/graphite/storage/log/webapp  
  
# Setup DB for graphite webapp  
RUN cd /opt/graphite/webapp/graphite && \  
python manage.py syncdb --noinput  
  
RUN chown -R www-data:www-data /opt/graphite  
  
# Install and configure statsd  
RUN git clone https://github.com/etsy/statsd.git /opt/statsd && \  
cd /opt/statsd && \  
npm install && \  
cp /tmp/src/config.js /opt/statsd/  
  
# Install supervisord config  
RUN cp /tmp/src/supervisord.conf /etc/supervisor/conf.d/  
  
# Cleanup  
RUN rm -rf /tmp/src/  
  
EXPOSE 80 8125/udp 2003 2004 7002  
CMD ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  

