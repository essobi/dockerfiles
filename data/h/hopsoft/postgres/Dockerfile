FROM phusion/baseimage:0.9.15  
MAINTAINER Nathan Hopkins <natehop@gmail.com>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7FCC7D46ACCC4CF8  
RUN echo deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg
main > /etc/apt/sources.list.d/pgdg.list  
RUN apt-add-repository -y ppa:georepublic/pgrouting  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y --force-yes install \  
build-essential \  
postgresql-9.3 \  
postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
postgresql-9.3-postgis-2.1 \  
postgresql-9.3-pgrouting \  
libpq-dev  
  
ADD conf/init.sh /etc/my_init.d/init.sh  
ADD conf/run.sh /etc/service/postgres/run  
ADD conf/logrotate /etc/logrotate.d/postgres  
  
RUN apt-get clean  

