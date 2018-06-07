# Container for MariaDB 10.1  
FROM tcaxias/debian  
MAINTAINER Tiago Caxias http://github.com/tcaxias  
  
ENV \  
PKGS="percona-toolkit" \  
DEPS="ca-certificates"  
  
RUN \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 9334A25F8507EFA5 && \  
echo 'deb [arch=amd64] http://repo.percona.com/apt jessie main' \  
> /etc/apt/sources.list.d/percona.list && \  
$APT update && \  
$APT upgrade && \  
$APT install $PKGS $DEPS && \  
$APT purge $DEPS && \  
apt-get -yqq autoremove && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/lib/mysql/* && \  
find / -name "*.a" -exec rm -f {} \;  

