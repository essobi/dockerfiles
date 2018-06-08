FROM debian:jessie-slim  
  
RUN apt-get -qq update  
RUN apt-get install -y wget base-files lsb-release lsb-base  
RUN wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release
-sc)_all.deb  
RUN dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb  
RUN apt-get update  
RUN apt-get install -y percona-xtrabackup-24  
RUN apt-get install -y nmap dnsutils iputils-ping

