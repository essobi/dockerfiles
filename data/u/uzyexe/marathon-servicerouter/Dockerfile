FROM python:2.7.10-slim  
  
ENV MARATHON_VERSION 0.11.1  
ENV HAPROXY_VERSION 1.5.8-3+deb8u2  
  
# install haproxy and mercurial and rsyslog  
RUN apt-get update -qq && \  
apt-get install -qfy haproxy=${HAPROXY_VERSION} mercurial rsyslog --no-
install-recommends && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
# install devcron  
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron
requests && \  
apt-get remove --purge -y mercurial  
  
# download marathon code  
ADD https://github.com/mesosphere/marathon/archive/v${MARATHON_VERSION}.tar.gz
marathon.tar.gz  
RUN mkdir marathon && \  
tar xvzf marathon.tar.gz -C marathon --strip-components 1 && \  
rm marathon.tar.gz  
  
# Setup defaults  
RUN mkdir /cron && \  
echo "* * * * * /cron/servicerouter.sh" > /cron/crontab && \  
echo "/marathon/bin/servicerouter.py --marathon http://127.0.0.1:8080" >
/cron/servicerouter.sh && \  
chmod a+x /cron/servicerouter.sh && \  
mkdir /var/log/haproxy  
  
ADD rsyslog-haproxy.conf /etc/rsyslog.d/49-haproxy.conf  
ADD logrotate-haproxy.conf /etc/logrotate.d/haproxy  
  
VOLUME ["/cron"]  
  
CMD service rsyslog start; \  
/usr/local/bin/devcron.py /cron/crontab  
  
EXPOSE 80 443 9090  

