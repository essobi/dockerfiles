FROM ubuntu:14.04  
MAINTAINER mick@twomeylee.name  
  
# Based on http://docs.docker.io/examples/postgresql_service/  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/postgresql.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& apt-get update \  
&& apt-get install -y -q \  
libpq-dev \  
postgresql-9.3 \  
postgresql-9.3-postgis-2.1 \  
postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
postgresql-server-dev-9.3 \  
&& apt-get autoclean \  
&& apt-get clean  
  
ADD postgresql-create-instance.sh /usr/local/bin/postgresql-create-instance.sh  
  
RUN chmod 755 /usr/local/bin/postgresql-create-instance.sh \  
&& mkdir -p /postgresql \  
&& chown postgres /postgresql  
  
USER postgres  
  
EXPOSE 5432  
VOLUME ["/postgresql/log", "/postgresql/data", "/postgresql/xlog"]  
  
CMD ["-D", "/postgresql/data", "-h", "0.0.0.0", "-p", "5432"]  
ENTRYPOINT ["/usr/lib/postgresql/9.3/bin/postgres"]  

