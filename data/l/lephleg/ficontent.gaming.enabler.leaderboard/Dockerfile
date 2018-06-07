FROM maven:3.3.1-jdk-7  
RUN apt-get -y update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install apg mysql-server wget
netcat \  
&& wget
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego -P /usr/local/bin \  
&& chmod +x /usr/local/bin/forego  
  
WORKDIR /root/target  
  
COPY . /root  
  
ENV MYSQL_ROOT_PASSWORD=''  
RUN cd .. \  
&& sed -i 's/^logfile/# logfile/g' bin/config.properties \  
&& cp bin/config.properties . \  
&& rm /etc/mysql/my.cnf \  
&& ln -s /root/etc/my.cnf /etc/mysql/my.cnf \  
&& mv etc/waitForPort*.sh /usr/local/bin/ \  
&& rm -rf /var/lib/mysql /var/log/mysql* \  
&& mvn package  
  
EXPOSE 4567  
CMD ["/root/etc/container-entrypoint.sh"]

