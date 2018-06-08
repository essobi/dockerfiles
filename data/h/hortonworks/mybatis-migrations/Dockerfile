FROM java:openjdk-7u79-jre  
  
MAINTAINER SequenceIQ  
  
RUN apt-get update  
RUN apt-get install -y netcat  
  
ADD https://github.com/mybatis/migrations/releases/download/mybatis-
migrations-3.2.0/mybatis-migrations-3.2.0.zip /opt/mybatis-
migrations-3.2.0.zip  
  
# Unpack the distribution  
RUN unzip /opt/mybatis-migrations-3.2.0.zip -d /opt/  
RUN rm -f /opt/mybatis-migrations-3.2.0.zip  
RUN chmod +x /opt/mybatis-migrations-3.2.0/bin/migrate  
  
RUN mkdir -p /migrate/drivers  
RUN mkdir -p /migrate/environments  
  
# Get the postgres JDBC driver from http://jdbc.postgresql.org/download.html  
ADD https://jdbc.postgresql.org/download/postgresql-9.4-1201.jdbc4.jar
/migrate/drivers/  
  
# Add command scripts  
ADD migrate.sh /opt/migrate.sh  
RUN chmod +x /opt/migrate.sh  
  
WORKDIR /migrate  
  
ENTRYPOINT ["/opt/migrate.sh"]  

