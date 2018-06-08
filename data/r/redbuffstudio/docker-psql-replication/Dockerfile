FROM ubuntu:14.04  
MAINTAINER Boyan Bonev <b.bonev@redbuffstudio.com>  
  
#Setup container environment parameters  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
#Configure locale.  
RUN locale-gen en_US en_US.UTF-8 && apt-get -y update  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
#Postgres paths.  
ENV PSQL_VERSION 9.4  
ENV PSQL_PATH /var/lib/postgresql  
ENV PSQL_DATA $PSQL_PATH/data  
ENV PATH $PSQL_PATH/$PSQL_VERSION/bin:$PATH  
  
#Prepare tools.  
RUN apt-get -y update && apt-get -y install wget  
  
#Install postgres  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo
apt-key add - \  
&& apt-get -y update \  
&& apt-get install -y postgresql-${PSQL_VERSION} postgresql-
contrib-${PSQL_VERSION} postgresql-common  
  
#Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf
/var/cache/apt/archives/*  
  
ADD ./bin/boot.sh /  
RUN chmod 755 /boot.sh  
  
VOLUME $PSQL_DATA  
  
EXPOSE 5432  
ENTRYPOINT ["/boot.sh"]  
CMD ["psql:run"]

