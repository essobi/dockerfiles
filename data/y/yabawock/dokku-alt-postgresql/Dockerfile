FROM phusion/baseimage:0.9.17  
MAINTAINER Morton Jonuschat <m.jonuschat@mojocode.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -qy --no-install-recommends --fix-missing --force-yes install wget
strace lsof netcat && \  
update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \  
curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&
\  
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list' && \  
apt-get update && \  
apt-get install -yq postgresql-9.4=9.4.5-1.pgdg14.04+1 postgresql-
contrib-9.4=9.4.5-1.pgdg14.04+1 postgresql-9.4-pgextwlist=1.3-3.pgdg14.04+1 &&
\  
apt-get clean && \  
apt-get autoremove -y  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Set default environment  
RUN mkdir -p /etc/container_environment  
ADD container_environment /etc/container_environment  
  
# Startup jobs  
RUN mkdir -p /etc/my_init.d  
ADD my_init.d /etc/my_init.d  
  
# Service: postgresql  
RUN mkdir -p /etc/service/postgresql/log/main  
ADD configs/postgresql.conf /etc/postgresql/9.4/main/postgresql.conf  
ADD configs/pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
ADD runit/postgresql /etc/service/postgresql/run  
ADD runit/log /etc/service/postgresql/log/run  

