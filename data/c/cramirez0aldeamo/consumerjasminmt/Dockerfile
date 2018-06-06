FROM debian:jessie  
  
MAINTAINER Jookies LTD <jasmin@jookies.net>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r jasmin && useradd -r -g jasmin jasmin \  
&& groupadd -r celuman && useradd -r -g celuman celuman  
  
ENV JASMIN_VERSION 0.9.26  
# Install requirements  
RUN apt-get update && apt-get install -y \  
python2.7 \  
python-pip \  
python-dev \  
libffi-dev \  
libssl-dev \  
rabbitmq-server \  
redis-server \  
nano \  
joe \  
vim \  
lsb \  
python-mysqldb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Jasmin SMS gateway  
RUN pip install redis && mkdir -p /etc/jasmin/resource \  
/etc/jasmin/store \  
/var/log/jasmin \  
&& chown jasmin:jasmin /etc/jasmin/store /var/log/jasmin \  
#&& pip install redis \  
&& pip install
https://pypi.python.org/packages/py2.py3/p/pika/pika-0.10.0-py2.py3-none-
any.whl \  
&& pip install
https://pypi.python.org/packages/source/t/txAMQP/txAMQP-0.6.2.tar.gz \  
&& pip install service_identity \  
&& pip install lpthw.web \  
&& pip2 install pytz \  
&& pip install --pre jasmin=="$JASMIN_VERSION"  
  
RUN mkdir -p /home/celuman/properties /home/celuman/scripts \  
&& mkdir -p /logs/archive && mkdir /home/celuman/bin \  
&& chown -R celuman:celuman /home/celuman/* \  
&& cp /etc/cron.daily/logrotate /etc/cron.hourly/  
  
EXPOSE 8080  
VOLUME ["/home/celuman/", "/logs"]  
  
COPY logrotate/logrotateContainer /etc/logrotate.d  
COPY bash/startConsumers.sh /home/celuman/bin  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh && chmod +x
/home/celuman/bin/startConsumers.sh  
RUN echo "*/10 * * * * bash /home/celuman/bin/startConsumers.sh >>
/logs/generalConsumer.log" >> celuman_cron \  
&& echo "0 1 * * * /usr/sbin/logrotate --force
/etc/logrotate.d/logrotateContainer" >> celuman_cron \  
&& crontab -u root celuman_cron && rm celuman_cron  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["python","/home/celuman/scripts/ClientStart.py"]  

