FROM fedora  
MAINTAINER Lars Kellogg-Stedman <lars@oddbit.com>  
  
RUN yum -y install graphite-web logrotate; yum clean all  
  
VOLUME /var/lib/graphite-web  
VOLUME /var/lib/carbon  
VOLUME /var/log  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/run-apache.sh"]  
  
ENV GRAPHITE_SECRET_KEY=UNSAFE_DEFAULT  
ENV GRAPHITE_TIME_ZONE=UTC  
  
COPY entrypoint.sh /entrypoint.sh  
COPY run-apache.sh /run-apache.sh  
RUN rm -f /etc/graphite-web/local_settings.py  
COPY local_settings.py /etc/graphite-web/local_settings.py.in  
COPY graphite-web.conf /etc/httpd/conf.d/graphite-web.conf  
COPY logs.conf /etc/httpd/conf.d/logs.conf  
  
RUN chmod a+x /entrypoint.sh /run-apache.sh  
  

