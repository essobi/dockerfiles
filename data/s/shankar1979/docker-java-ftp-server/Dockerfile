FROM anapsix/alpine-java  
  
#download the Apache FTP server & extract  
RUN apk add --update tar && \  
wget http://apache.osuosl.org/mina/ftpserver/1.1.1/dist/apache-
ftpserver-1.1.1.tar.gz \  
&& tar -xzvf apache-ftpserver-1.1.1.tar.gz  
  
#set base direectory  
WORKDIR "/apache-ftpserver-1.1.1"  
  
#Add the config file. FtpServer needs a basic config file.  
ADD ftpd.xml ftpd.xml  
  
#Add a test file. In this optional step, we can add several test files.  
ADD hello.txt hello.txt  
  
CMD ["bin/ftpd.sh", "ftpd.xml"]  

