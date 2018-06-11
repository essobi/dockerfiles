FROM centos:centos6  
  
MAINTAINER Abed Halawi <abed.halawi@vinelab.com>  
  
# update packages  
RUN yum -y update  
  
# install basic software  
RUN yum install -y rsyslog vixie-cron vim wget tar  
  
# make the terminal prettier  
RUN echo 'export PS1="[\u@docker] \W # "' >> /root/.bash_profile  
  
# install & configure supervisord  
RUN yum -y install http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
RUN /usr/bin/echo_supervisord_conf > /etc/supervisord.conf  
RUN mkdir -p /var/log/supervisord  
  
# make supervisor run in foreground  
RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf  
  
# make supervisor run the http server on 9001  
RUN sed -i -e "s/^;\\[inet_http_server\\]/\\[inet_http_server\\]/"
/etc/supervisord.conf  
RUN sed -i -e "s/^;port=127.0.0.1:9001/port=0.0.0.0:9001/"
/etc/supervisord.conf  
RUN sed -i -e "s/^;username=user/username=vinelab/" /etc/supervisord.conf  
RUN sed -i -e "s/^;password=123/password=vinelab/" /etc/supervisord.conf  
  
# tell supervisor to include relative .ini files  
RUN mkdir /etc/supervisord.d  
RUN echo [include] >> /etc/supervisord.conf  
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf  
  
# add programs to supervisord config  
ADD ini/rsyslog.ini /etc/supervisord.d/rsyslog.ini  
ADD ini/cron.ini /etc/supervisord.d/cron.ini  
  
RUN yum clean all  
  
# setup locale  
RUN echo 'LANG=C' > /etc/sysconfig/i18n  
  
ADD run /  
RUN chmod +x /run  
  
EXPOSE 9001  
CMD /run  

