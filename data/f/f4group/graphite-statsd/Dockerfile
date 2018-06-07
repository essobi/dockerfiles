FROM phusion/baseimage:0.9.19  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
RUN add-apt-repository -y ppa:pypy/ppa  
  
#RUN echo deb http://archive.ubuntu.com/ubuntu $(lsb_release -cs) main
universe > /etc/apt/sources.list.d/universe.list  
RUN apt-get -y update\  
&& apt-get -y upgrade  
  
# dependencies  
RUN apt-get -y --force-yes install vim\  
nginx\  
python-virtualenv\  
pypy\  
pypy-dev\  
expect\  
git\  
memcached\  
sqlite3\  
libcairo2\  
libcairo2-dev\  
pkg-config\  
nodejs  
  
# workaround Django bug (see https://code.djangoproject.com/ticket/16017)  
ENV LANG "en_US.UTF-8"  
RUN virtualenv -p /usr/bin/pypy /srv/graphite-pypy  
  
ENV VIRTUAL_ENV=/srv/graphite-pypy  
ENV PATH=/srv/graphite-
pypy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ONBUILD ENV VIRTUAL_ENV=/srv/graphite-pypy  
ONBUILD ENV PATH=/srv/graphite-
pypy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# python dependencies  
RUN pip install django==1.5\  
python-memcached==1.53\  
django-tagging==0.3.1\  
twisted==11.1.0\  
txAMQP==0.6.2\  
flup==1.0.2\  
cairocffi==0.7.2  
  
# install graphite  
RUN git clone -b 0.9.15-1 --depth 1 https://github.com/F4-group/graphite-
web.git /usr/local/src/graphite-web  
WORKDIR /usr/local/src/graphite-web  
RUN python ./setup.py install  
ADD scripts/local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
ADD conf/graphite/ /opt/graphite/conf/  
  
# install whisper  
RUN git clone -b 0.9.15 --depth 1 https://github.com/graphite-
project/whisper.git /usr/local/src/whisper  
WORKDIR /usr/local/src/whisper  
RUN python ./setup.py install  
  
# install carbon  
RUN git clone -b 0.9.15 --depth 1 https://github.com/graphite-
project/carbon.git /usr/local/src/carbon  
WORKDIR /usr/local/src/carbon  
RUN python ./setup.py install  
  
# install statsd  
RUN git clone -b v0.7.2 --depth 1 https://github.com/etsy/statsd.git
/opt/statsd  
ADD conf/statsd/config.js /opt/statsd/config.js  
  
# config nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD conf/nginx/graphite.conf /etc/nginx/sites-available/graphite.conf  
RUN ln -s /etc/nginx/sites-available/graphite.conf /etc/nginx/sites-
enabled/graphite.conf  
  
# init django admin  
ADD scripts/django_admin_init.exp /usr/local/bin/django_admin_init.exp  
RUN /usr/local/bin/django_admin_init.exp  
  
# logging support  
RUN mkdir -p /var/log/carbon /var/log/graphite /var/log/nginx  
ADD conf/logrotate /etc/logrotate.d/graphite  
RUN chmod 644 /etc/logrotate.d/graphite  
  
# daemons  
ADD daemons/carbon.sh /etc/service/carbon/run  
ADD daemons/carbon-aggregator.sh /etc/service/carbon-aggregator/run  
ADD daemons/graphite.sh /etc/service/graphite/run  
ADD daemons/statsd.sh /etc/service/statsd/run  
ADD daemons/nginx.sh /etc/service/nginx/run  
  
# migration scripts  
RUN mkdir -p /etc/my_init.d  
ADD scripts/migrate_db_0.9.14.sh /etc/my_init.d/migrate_db_0.9.14.sh  
  
# cleanup  
RUN apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# defaults  
EXPOSE 80:80 2003:2003 8125:8125/udp  
VOLUME ["/opt/graphite", "/etc/nginx", "/opt/statsd", "/etc/logrotate.d",
"/var/log"]  
ENV HOME /root  
CMD ["/sbin/my_init"]  

