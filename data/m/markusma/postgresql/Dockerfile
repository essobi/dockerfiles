# PostgreSQL 9.4 with PostGIS 2.1 on Ubuntu Trusty  
#  
# Included plugins:  
# pgextwlist  
FROM markusma/ubuntu:trusty  
  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 7FCC7D46ACCC4CF8 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends postgresql-9.4 postgresql-
contrib-9.4 postgresql-server-dev-9.4 git build-essential language-pack-fi
postgresql-9.4-postgis-2.1 \  
&& dpkg-reconfigure locales \  
&& cd /tmp \  
&& git clone https://github.com/dimitri/pgextwlist.git \  
&& cd pgextwlist \  
&& make \  
&& make install \  
&& mkdir -p /usr/lib/postgresql/9.4/lib/plugins \  
&& cp pgextwlist.so /usr/lib/postgresql/9.4/lib/plugins \  
&& cd / \  
&& rm -rf /tmp/pgextwlist \  
&& apt-get purge -y postgresql-server-dev-9.4 git build-essential \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -L https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64
-o /usr/local/bin/gosu \  
&& chmod +x /usr/local/bin/gosu  
  
COPY etc/ /etc/  
COPY bin/ /usr/local/bin/  
  
EXPOSE 5432  
VOLUME ["/var/lib/postgresql/9.4/main"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D",
"/var/lib/postgresql/9.4/main", "-c",
"config_file=/etc/postgresql/9.4/main/postgresql.conf"]  

