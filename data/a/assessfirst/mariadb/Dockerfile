FROM mariadb:latest  
MAINTAINER Julien Houvion "jhouvion@assessfirst.com"  
  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y sudo wget perl && \  
apt-get -q autoremove && \  
apt-get -q clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /var/cache/apt/*.bin  
  
RUN mkdir /opt/mysqltuner && \  
cd /opt/mysqltuner && \  
wget http://mysqltuner.pl/ -O mysqltuner.pl && \  
wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/basic_passwords.txt -O basic_passwords.txt && \  
wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/vulnerabilities.csv -O vulnerabilities.csv  
  
  
ADD mysqltuner /usr/local/bin/mysqltuner  
  
RUN chmod +x /usr/local/bin/mysqltuner  
  
  
  
  
  
  
  
  

