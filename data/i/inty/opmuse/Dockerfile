FROM debian:jessie  
MAINTAINER Mattias Fliesberg <mattias@fliesberg.email>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# we need contrib and non-free for curl, unrar and stuff  
RUN sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y curl wget locales  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN dpkg-reconfigure locales  
  
RUN echo "deb http://apt.opmu.se/debian/ master main" >
/etc/apt/sources.list.d/opmuse.list  
RUN curl -s http://apt.opmu.se/opmuse.pub | apt-key add -  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >
/etc/apt/sources.list.d/deb-multimedia.list  
RUN wget -q https://www.deb-multimedia.org/pool/main/d/deb-multimedia-
keyring/deb-multimedia-keyring_2016.3.7_all.deb  
RUN dpkg -i deb-multimedia-keyring_2016.3.7_all.deb  
RUN apt-get update  
  
RUN echo "mysql-server mysql-server/root_password password" | debconf-set-
selections  
RUN echo "mysql-server mysql-server/root_password_again password" | debconf-
set-selections  
  
# we need mysqld running for dbconfig-common to work,  
# so we disable the policy-rc.d nonsense  
RUN rm /usr/sbin/policy-rc.d  
  
RUN apt-get install -y opmuse  
  
VOLUME ["/var/lib/mysql", \  
"/etc/opmuse", \  
"/var/cache/opmuse", \  
"/var/log/opmuse"]  
  
COPY scripts/docker-start.sh /home/opmuse/start.sh  
  
ENTRYPOINT ["/home/opmuse/start.sh"]  
  
EXPOSE 8080  

