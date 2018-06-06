FROM ubuntu:xenial  
MAINTAINER Sascha Wessel <swessel@gr4yweb.de>  
  
# Update System  
RUN apt-get update -y && apt-get upgrade -y  
  
# Install Dependencies  
RUN apt-get install -y python-ldap python-cairo python-django python-twisted
python-django-tagging python-simplejson python-memcache python-pysqlite2
python-tz python-pip supervisor  
RUN pip install whisper==1.0.1  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon==1.0.1  
  
# Create Directories  
RUN mkdir -p /data/graphite/storage/whisper  
RUN touch /data/graphite/storage/graphite.db /data/graphite/storage/index  
RUN chmod 0775 /data/graphite/storage /data/graphite/storage/whisper  
RUN chmod 0664 /data/graphite/storage/graphite.db  
  
# Add Config file  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
#ADD carbon.conf /data/graphite/conf/carbon.conf  
#ADD storage-schemas.conf /data/graphite/conf/storage-schemas.conf  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Carbon line receiver port  
EXPOSE 2003  
# Carbon UDP receiver port  
EXPOSE 2003/udp  
# Carbon pickle receiver port  
EXPOSE 2004  
# Carbon cache query port  
EXPOSE 7002  
# Volumes  
VOLUME ["/data/graphite"]  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/usr/local/bin/entrypoint.sh"]  

