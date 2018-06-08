FROM linuxserver/baseimage  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
MAINTAINER Mark Burford <sparklyballs@gmail.com>  
ENV HOME /root  
ENV POSTGRES_USER abc  
ENV PGDATA /config/databases  
ENV PG_MAJOR 9.4  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Set the locale  
RUN locale-gen en_US.UTF-8  
  
# Install Postgres  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update -q && \  
apt-get install \  
postgresql-common -qy && \  
sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf && \  
apt-get install \  
postgresql-$PG_MAJOR \  
postgresql-client-$PG_MAJOR \  
postgresql-contrib-$PG_MAJOR -qy && \  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
#Adding abc user  
RUN useradd -u 911 -U -s /bin/false abc && usermod -G users abc  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
RUN chmod -v +x /etc/service/*/run && chmod -v +x /etc/my_init.d/*.sh  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Volumes and Ports  
VOLUME /config  
EXPOSE 5432  

