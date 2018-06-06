FROM debian:9  
MAINTAINER Benoit Chabord <>  
  
ENV MCS_MAJOR_VERSION "1.0.11"  
ENV MCS_MINOR_VERSION "-1"  
WORKDIR /root/  
EXPOSE 3306  
VOLUME /usr/local/mariadb/columnstore/etc  
VOLUME /usr/local/mariadb/columnstore/data1  
VOLUME /usr/local/mariadb/columnstore/mysql/db  
  
RUN apt-get update \  
&& apt-get -y install wget expect perl openssl file sudo runit rsyslog \  
&& apt-get -y install libdbi-perl libboost-all-dev libreadline-dev \  
&& apt-get -y install rsync libsnappy1v5 net-tools libdbd-mysql-perl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY service /etc/service/  
COPY entrypoint.sh /root/entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  
  
RUN mkdir /root/install/ && cd /root/install \  
&& wget
https://downloads.mariadb.com/ColumnStore/$MCS_MAJOR_VERSION/debian/dists/stretch/main/binary_amd64/mariadb-
columnstore-$MCS_MAJOR_VERSION$MCS_MINOR_VERSION-stretch.x86_64.deb.tar.gz \  
&& tar -xvf *.tar.gz && dpkg -i *.deb && rm -rf /root/install \  
&& chmod 755 /etc/service/systemd-journald/run /etc/service/rsyslogd/run
/etc/service/columnstore/run /root/entrypoint.sh  
  

