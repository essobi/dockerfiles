FROM ubuntu  
MAINTAINER Juan José Orjuela <j.j.o.c007@gmail.com>  
  
  
RUN apt-get update && apt-get -y install default-jdk wget zip git vim
postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5 software-
properties-common  
  
RUN mkdir /var/liquibase && mkdir /var/liquidbase-oas  
  
RUN chmod 777 -R /var/liquibase  
RUN chmod 777 -R /var/liquidbase-oas  
  
RUN wget https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-3.5.1/liquibase-3.5.1-bin.zip && unzip liquibase-3.5.1-bin.zip -d
/var/liquibase  
  
ADD postgresql-JDBC.jar /var/liquibase/lib  
  
USER postgres  
  
RUN /etc/init.d/postgresql start && psql --command "ALTER USER postgres
PASSWORD '123456';" && createdb -O postgres OAS-API  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.5/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf  
  
EXPOSE 5432  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
RUN git clone https://github.com/jjoc007/oas-liquidbase.git /var/liquidbase-
oas  
RUN /etc/init.d/postgresql start && /var/liquidbase-oas/./oas-liquidbase.sh

