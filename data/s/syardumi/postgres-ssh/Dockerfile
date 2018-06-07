# vim:set ft=dockerfile:  
FROM debian:jessie  
  
# explicitly set user/group IDs  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y --auto-remove ca-certificates wget  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
ENV PG_MAJOR 9.4  
ENV PG_VERSION 9.4.5-1.pgdg80+1  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgresql-$PG_MAJOR=$PG_VERSION \  
postgresql-contrib-$PG_MAJOR=$PG_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
#SSH  
RUN echo "deb http://ftp.us.debian.org/debian jessie main" | tee -a
/etc/apt/sources.list  
RUN echo "deb-src http://ftp.us.debian.org/debian jessie main" | tee -a
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y install openssh-server wget  
RUN mkdir /var/run/sshd  
RUN sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/"
/etc/ssh/sshd_config  
  
#keys  
RUN mkdir -p /root/.ssh  
RUN chmod 700 /root/.ssh  
RUN chown root:root /root/.ssh  
RUN wget -O /root/.ssh/authorized_keys
"https://github.com/syardumi/postgres/blob/master/insecure_key.pub"  
RUN chmod 600 /root/.ssh/authorized_keys  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 22 5432  
CMD ["postgres"]  

