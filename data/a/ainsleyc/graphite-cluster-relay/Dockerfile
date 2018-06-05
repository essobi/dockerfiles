FROM ainsleyc/graphite-cluster-base  
MAINTAINER Ainsley Chong <ainsley.chong@gmail.com>  
  
# install graphite  
RUN git clone -b 0.9.12 https://github.com/graphite-project/graphite-web.git
/usr/local/src/graphite-web  
WORKDIR /usr/local/src/graphite-web  
RUN python ./setup.py install  
ADD scripts/local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
ADD conf/graphite/ /opt/graphite/conf/  
  
# install whisper  
RUN git clone -b 0.9.12 https://github.com/graphite-project/whisper.git
/usr/local/src/whisper  
WORKDIR /usr/local/src/whisper  
RUN python ./setup.py install  
  
# install carbon  
RUN git clone -b 0.9.12 https://github.com/graphite-project/carbon.git
/usr/local/src/carbon  
WORKDIR /usr/local/src/carbon  
RUN python ./setup.py install  
  
# init django admin  
ADD scripts/django_admin_init.exp /usr/local/bin/django_admin_init.exp  
RUN /usr/local/bin/django_admin_init.exp  
  
# logging support  
RUN mkdir -p /var/log/carbon /var/log/graphite /var/log/nginx  
ADD conf/logrotate /etc/logrotate.d/graphite  
RUN chmod 644 /etc/logrotate.d/graphite  
  
# daemons  
ADD daemons/carbon-relay.sh /etc/service/carbon-relay/run  
  
# scripts  
ADD scripts/build_configs /sbin/build_configs  
  
# cleanup  
RUN apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# defaults  
ENV HOME /root  
CMD ["/sbin/build_configs"]  

