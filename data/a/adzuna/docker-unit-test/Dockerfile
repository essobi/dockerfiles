FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV PERL5LIB /adzuna  
ENV BOX docker-container  
ENV DBIC_DT_SEARCH_OK 1  
ADD files/environment /etc/adzuna/environment  
ADD files/system-source.list /etc/apt/sources.list  
ADD files/adzuna-source.list /etc/apt/sources.list.d/adzuna-code.list  
  
RUN apt-get update  
ADD files/system-deb.packages /tmp/system-deb.packages  
RUN apt-get install -y --force-yes $(cat /tmp/system-deb.packages); rm
/tmp/system-deb.packages  
  
ADD files/perl5-deb.packages /tmp/perl5-deb.packages  
RUN apt-get install -y --force-yes $(cat /tmp/perl5-deb.packages); rm
/tmp/perl5-deb.packages  
  
RUN mkdir /var/log/adzuna  
  
## dumb-init is a simple process supervisor and init system designed to run as
PID 1 inside minimal container environments (such as Docker). It is deployed
as a small, statically-linked binary written in C.  
## Lightweight containers have popularized the idea of running a single
process or service without normal init systems like systemd or sysvinit.
However, omitting an init system often leads to incorrect handling of
processes and signals, and can result in problems such as containers which
can't be gracefully stopped, or leaking containers which should have been
destroyed.  
## dumb-init enables you to simply prefix your command with dumb-init. It acts
as PID 1 and immediately spawns your command as a child process, taking care
to properly handle and forward signals as they are received.  
## https://github.com/Yelp/dumb-init  
RUN wget -cO /tmp/dumb-init.deb https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb  
RUN dpkg -i /tmp/dumb-init.deb  
  
VOLUME [ "/adzuna", "/srv/adzuna/data/uas" ]  
  
WORKDIR /adzuna  
  
ENTRYPOINT [ "/usr/bin/dumb-init", "--" ]  

