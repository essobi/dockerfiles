FROM glassfish:4.1  
MAINTAINER Daniel Bustamante Ospina "dbustamante69@gmail.com"  
#Install Mysql Driver  
RUN wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.35.zip \  
&& unzip mysql-connector-java-5.1.35.zip mysql-connector-java-5.1.35/mysql-
connector-java-5.1.35-bin.jar \  
&& cp mysql-connector-java-5.1.35/mysql-connector-java-5.1.35-bin.jar
glassfish/domains/domain1/lib/ext/ \  
&& rm -rf mysql-connector-java-5.1.35*  

