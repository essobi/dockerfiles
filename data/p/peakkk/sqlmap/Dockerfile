FROM python:2.7-alpine  
  
ENV REFRESHED_AT "2017-07-29 00:00:00"  
RUN set -ex \  
&& apk add \--no-cache git \  
&& git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /sqlmap \  
&& cd /sqlmap \  
&& ln -s /sqlmap/sqlmap.py /usr/bin/sqlmap  
  
WORKDIR /sqlmap  
VOLUME /root/.sqlmap/  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/sh"]  

