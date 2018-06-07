FROM infraops/debian  
MAINTAINER anderson@infraops.info  
  
env FASTCGI=false  
env WEBDAV=false  
env SEAFILE_NAME=  
env SEAFILE_ADDRESS=  
env SEAFILE_ADMIN=  
env SEAFILE_ADMIN_PW=  
env MYSQL_SERVER=  
env MYSQL_USER=  
env MYSQL_USER_PASSWORD=  
env MYSQL_ROOT_PASSWORD=  
  
RUN mkdir -p /opt/seafile /cloud /seafile \  
&& useradd -d /seafile -M -s /bin/bash -c "Seafile User" seafile \  
&& ls -lld /seafile \  
&& id seafile  
  
RUN curl -sL $(curl -sL https://www.seafile.com/en/download/ \  
| grep -oE 'https://.*seafile-server_6.1.0_x86-64.tar.gz'|sort -r|head -1) \  
| tar -C /opt/seafile/ -xz \  
&& chown -R seafile:seafile /cloud /opt/seafile /seafile \  
&& ls -l /opt/seafile/seafile*-server*/  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y python2.7 libpython2.7 python-mysqldb \  
python-setuptools python-imaging python-ldap sqlite3 \  
python-memcache mysql-client supervisor poppler-utils libnss3 ffmpeg \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN easy_install pip  
RUN pip install boto requests pillow moviepy  
  
COPY seafile-entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 8000 8081 8082  
VOLUME ["/cloud"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

