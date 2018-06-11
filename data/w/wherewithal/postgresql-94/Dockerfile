FROM phusion/baseimage:0.9.16  
MAINTAINER hosh@getwherewithal.com  
  
ENV PG_VERSION 9.4  
#RUN apt-get update && apt-get install -y wget  
#RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add - \  
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update \  
&& apt-get install -y postgresql-${PG_VERSION} postgresql-client-${PG_VERSION}
postgresql-contrib-${PG_VERSION} \  
&& mkdir /etc/service/postgresql-9.4 \  
&& rm -rf /var/lib/postgresql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD conf/postgresql.conf /etc/postgresql/9.4/main/postgresql.conf  
ADD conf/pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
ADD postgresql.runit /etc/service/postgresql-9.4/run  
RUN chmod 755 /etc/service/postgresql-9.4/run  
  
EXPOSE 5432  
VOLUME ["/var/lib/postgresql"]  
VOLUME ["/run/postgresql"]  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

