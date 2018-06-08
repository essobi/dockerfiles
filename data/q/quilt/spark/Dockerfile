From ubuntu  
Maintainer Ethan J. Jackson  
  
RUN apt-get update && apt-get install -y \  
default-jre-headless \  
python-minimal \  
wget \  
&& wget -qO- http://www-us.apache.org/dist/spark/spark-1.6.1/spark-1.6.1-bin-
hadoop2.6.tgz | tar -xzf - \  
&& mv /spark* /spark \  
&& wget -qO- https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz | tar -xzf - \  
&& mv /mysql-connector-java* /mysql-connector-java \  
&& apt-get remove \--purge -y wget \  
&& apt-get autoremove \--purge -y \  
&& rm -rf /var/lib/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /spark/sbin:/spark/bin:$PATH  
  
Copy run /bin/  
Copy log4j.properties /spark/conf  

