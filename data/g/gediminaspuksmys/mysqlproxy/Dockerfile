FROM pataquets/ubuntu:trusty  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN wget https://downloads.mysql.com/archives/get/file/mysql-
proxy-0.8.5-linux-debian6.0-x86-64bit.tar.gz && \  
tar -xzvf mysql-proxy-0.8.5-linux-debian6.0-x86-64bit.tar.gz && \  
mv mysql-proxy-0.8.5-linux-debian6.0-x86-64bit /opt/mysql-proxy && \  
rm mysql-proxy-0.8.5-linux-debian6.0-x86-64bit.tar.gz  
  
RUN chown -R root:root /opt/mysql-proxy  
  
EXPOSE 3306  
ADD run.sh /opt/run.sh  
RUN chmod u+x /opt/run.sh  
  
ENTRYPOINT [ "/opt/run.sh" ]  

