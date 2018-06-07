FROM factual/docker-cdh5-base  
  
RUN apt-get update && apt-get install -y wget  
ENV PG_VERSION="9.5"  
ENV RUBY_VERSION="2.3"  
#postgres  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ "$(lsb_release
-sc)"-pgdg main" >> /etc/apt/sources.list.d/pgdg.list  
RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
# for ruby  
RUN apt-add-repository ppa:brightbox/ruby-ng  
  
RUN apt-get update && apt-get install -y postgresql-$PG_VERSION
ruby$RUBY_VERSION  
  
ADD pg_hba.conf /etc/postgresql/$PG_VERSION/main/pg_hba.conf  
ADD postgresql.conf /etc/postgresql/$PG_VERSION/main/postgresql.conf  
  
RUN mkdir -p /data  
  
VOLUME ["/data"]  
  
ADD configure_postgres.sh /etc/my_init.d/010_configure_postgres  
ADD bootstrap.sh /etc/my_init.d/099_bootstrap  
  
#cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD bootstrap.sh /etc/my_init.d/099_bootstrap  

