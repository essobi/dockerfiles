# vim:set ft=dockerfile:  
FROM postgres:9.4  
ENV TERM xterm-256color  
  
RUN echo deb http://ftp.us.debian.org/debian jessie main >>
/etc/apt/sources.list && \  
echo deb http://ftp.us.debian.org/debian jessie-backports main >>
/etc/apt/sources.list && \  
echo deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main >
/etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install git ca-certificates && \  
git clone https://github.com/tada/pljava.git && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install g++ maven && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install postgresql-server-dev-9.4 libpq-dev && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install libecpg-dev libkrb5-dev && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install oracle-java8-installer libssl-dev && \  
export PGXS=/usr/lib/postgresql/9.4/lib/pgxs/src/makefiles/pgxs.mk && \  
cd pljava && \  
git checkout tags/V1_5_0 && \  
mvn -Pwnosign clean install && \  
java -jar /pljava/pljava-packaging/target/pljava-pg9.4-amd64-Linux-gpp.jar &&
\  
cd ../ && \  
apt-get -y remove \--purge --auto-remove git ca-certificates g++ maven
postgresql-server-dev-9.4 libpq-dev libecpg-dev libkrb5-dev oracle-
java8-installer libssl-dev && \  
apt-get clean && apt-get update && apt-get \--fix-missing -y \--force-yes
--no-install-recommends install openjdk-8-jdk-headless && \  
apt-get -y clean autoclean autoremove && \  
rm -rf ~/.m2 /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD /docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 5432  
CMD ["postgres"]  

