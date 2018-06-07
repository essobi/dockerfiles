FROM debian:jessie  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y libipc-system-simple-perl mysql-client wget && \  
apt-get autoremove --purge -y && \  
apt-get clean && \  
rm -rvf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/share/mysqltuner && \  
wget http://mysqltuner.pl/ -O /usr/share/mysqltuner/mysqltuner.pl && \  
wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/basic_passwords.txt -O /usr/share/mysqltuner/basic_passwords.txt
&& \  
wget https://raw.githubusercontent.com/major/MySQLTuner-
perl/master/vulnerabilities.csv -O /usr/share/mysqltuner/vulnerabilities.csv  
  
ENTRYPOINT ["perl", "/usr/share/mysqltuner/mysqltuner.pl"]  

