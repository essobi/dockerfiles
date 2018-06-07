FROM phusion/baseimage:0.9.17  
MAINTAINER Markus Kosmal <code@m-ko-x.de>  
  
# Based upon paintedfox/docker-postgresql by Ryan Seto <ryanseto@yak.net>  
# and Postgresql (http://www.postgresql.org/)  
ENV POSTGRES_VERSION 9.3  
RUN apt-get -yqq update && DEBIAN_FRONTEND=noninteractive apt-get install -yqq
wget pwgen inotify-tools  
  
# prepare  
RUN locale-gen en_US.UTF-8 && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - \  
apt-get update -yqq  
  
# install  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -yqq --force-yes \  
postgresql-${POSTGRES_VERSION} postgresql-client-${POSTGRES_VERSION}
postgresql-contrib-${POSTGRES_VERSION} && \  
/etc/init.d/postgresql stop && \  
apt-get clean -yqq && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# configure  
RUN sed -i -e"s/data_directory =.*$/data_directory = '\/store'/"
/etc/postgresql/${POSTGRES_VERSION}/main/postgresql.conf && \  
sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/"
/etc/postgresql/${POSTGRES_VERSION}/main/postgresql.conf && \  
echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/${POSTGRES_VERSION}/main/pg_hba.conf  
  
# customizing  
ADD scripts /scripts  
RUN chmod +x /scripts/start.sh  
  
# daemonize  
RUN mkdir /etc/service/postgresql && \  
ln -s /scripts/start.sh /etc/service/postgresql/run  
  
# expose  
VOLUME ["/store"]  
EXPOSE 5432  
# run  
CMD ["/sbin/my_init"]  

