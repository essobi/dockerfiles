##  
# Multicorn 0.9.1 on Postgres 9.1  
##  
FROM ubuntu:12.04  
MAINTAINER Mike Douglas http://www.github.com/mike-douglas/  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
ENV DB_USER docker  
ENV DB_PASS docker  
ENV DB_NAME multicorn  
  
RUN apt-get install -y build-essential python-dev python-pip postgresql
postgresql-server-dev-9.1  
RUN pip install pgxnclient  
RUN pgxn install multicorn==0.9.1 --testing  
  
# Open Postgres ports  
RUN mkdir -p /etc/postgresql/9.1/main  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.1/main/pg_hba.conf  
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.1/main/postgresql.conf  
RUN echo "port = 5432" >> /etc/postgresql/9.1/main/postgresql.conf  
  
EXPOSE 5432  
ADD start.sh /start.sh  
RUN chmod a+x /start.sh  
  
VOLUME /src  
  
CMD ["/start.sh"]  

