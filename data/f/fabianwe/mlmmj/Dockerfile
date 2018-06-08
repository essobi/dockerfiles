FROM ubuntu:16.04  
MAINTAINER Fabian Wenzelmann <fabianwen@posteo.eu>  
  
# expect only required for the fix of mlmmj-make-ml  
RUN apt-get update && apt-get install -y cron curl tar bzip2 build-essential
python3 expect  
  
ENV PYTHONUNBUFFERED 0  
# create a spool directory for mlmmj and add mlmmj user  
# RUN groupadd mlmmj && useradd -g mlmmj mlmmj -d /var/spool/mlmmj -m && chown
-R mlmmj.mlmmj /var/spool/mlmmj  
# removed, we simply run as root... makes things easier...  
# set current mlmmj version  
ENV MLMMJ_VERSION 1.3.0  
ENV MLMMJ_PREFIX mlmmj-  
  
RUN curl -SLO "http://mlmmj.org/releases/mlmmj-$MLMMJ_VERSION.tar.bz2"  
RUN tar jxf mlmmj-$MLMMJ_VERSION.tar.bz2  
  
WORKDIR /$MLMMJ_PREFIX$MLMMJ_VERSION  
  
RUN ./configure && make && make install  
  
COPY mlmmj_listener.py /  
RUN chmod +x /mlmmj_listener.py  
  
COPY docker_entrypoint.sh /  
RUN chmod +x /docker_entrypoint.sh  
  
COPY renew_text.sh /  
RUN chmod +x /renew_text.sh  
  
COPY mk_ml /  
RUN chmod +x /mk_ml  
  
RUN mkdir /mlmmj_conf/  
# RUN chown -R mlmmj:mlmmj /mlmmj_conf/  
# RUN chown -R mlmmj:mlmmj /var/spool/mlmmj  
WORKDIR /var/spool/mlmmj  
RUN rm -rf /mlmmj-$MLMMJ_VERSION.tar.bz2 /$MLMMJ_PREFIX$MLMMJ_VERSION  
  
# add crontab for mlmmj-maintd  
COPY crontab /etc/cron.d/mlmmj-maintd-cron  
RUN chmod 0644 /etc/cron.d/mlmmj-maintd-cron  
RUN /usr/bin/crontab /etc/cron.d/mlmmj-maintd-cron  
  
EXPOSE 7777  
ENTRYPOINT ["/docker_entrypoint.sh"]  
CMD ["/mlmmj_listener.py"]  

