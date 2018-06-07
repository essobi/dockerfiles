FROM postgres:9.4  
MAINTAINER jm@epiclabs.io  
  
ENV POSTGRES_DB=postgres  
ENV POSTGRES_USER=docker  
ENV POSTGRES_PASSWORD=docker  
ENV MONOLITHIC_APPROACH=1  
# Install java7 for liquibase  
# Install dos2unix to cope with git windows crlf addition  
RUN apt-get update && apt-get install -y \  
openjdk-7-jre \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# liquibase  
RUN curl -L
https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-3.4.1/liquibase-3.4.1-bin.tar.gz -o /tmp/liquibase-3.4.1-bin.tar.gz  
  
# Create a directory for liquibase  
RUN mkdir /opt/liquibase  
  
# Unpack the distribution  
RUN tar -xzf /tmp/liquibase-3.4.1-bin.tar.gz -C /opt/liquibase  
RUN chmod +x /opt/liquibase/liquibase  
  
# Symlink to liquibase to be on the path  
RUN ln -s /opt/liquibase/liquibase /usr/local/bin/  
  
# cleanup  
RUN rm /tmp/liquibase-3.4.1-bin.tar.gz  
  
# Get the postgres JDBC driver from http://jdbc.postgresql.org/download.html  
RUN mkdir -p /opt/jdbc_drivers/liquibase/lib/  
RUN curl -L https://jdbc.postgresql.org/download/postgresql-9.4.1208.jre7.jar
-o /opt/jdbc_drivers/postgresql-9.4.1208.jre7.jar  
  
RUN ln -s /opt/jdbc_drivers/postgresql-9.4.1208.jre7.jar /usr/local/bin/  
  
ADD src/ /  
WORKDIR /  
RUN chmod +x *.sh  
RUN chmod -R +x /scripts  
  
#VOLUME ["/changelogs"]  
ENTRYPOINT ["/postgres-entrypoint.sh"]  
CMD ["postgres"]  

