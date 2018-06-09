FROM phusion/baseimage:0.9.18  
MAINTAINER xama <oliver@xama.us>  
ENV SEAFILE_VERSION 6.0.5  
EXPOSE 8082 8000  
RUN mkdir /seafile  
VOLUME /seafile  
WORKDIR /seafile  
  
# Required packages for pro edition  
RUN apt-get update && apt-get install -y \  
openjdk-7-jre poppler-utils libpython2.7 python-pip \  
python-setuptools python-imaging python-mysqldb python-memcache python-ldap \  
python-urllib3 sqlite3 wget \  
libreoffice libreoffice-script-provider-python fonts-vlgothic ttf-wqy-microhei
ttf-wqy-zenhei xfonts-wqy && pip install boto  
  
# Add custom configuration  
COPY seafevents.conf /seafevents.conf  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /seafile/seafile-server-latest/seafile.sh start && /seafile/seafile-
server-latest/seahub.sh start  

