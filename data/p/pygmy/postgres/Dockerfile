FROM pygmy/alpine-tini:3.7  
  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
  
ENV LANG en_US.utf8  
ENV PATH /usr/lib/postgresql/10/bin:$PATH  
ENV PGDATA /var/lib/postgresql/10/data  
  
RUN apk add --no-cache \  
postgresql \  
postgresql-contrib \  
su-exec \  
tzdata \  
bash \  
&& mkdir /docker-entrypoint-initdb.d \  
&& chown -R postgres:postgres /docker-entrypoint-initdb.d \  
&& chmod 777 /docker-entrypoint-initdb.d \  
&& mkdir /run/postgresql \  
&& chown -R postgres:postgres /run/postgresql \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
VOLUME /var/lib/postgresql/10/data  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  
  
EXPOSE 5432  
  
CMD ["postgres"]  

