FROM ubuntu:precise  
MAINTAINER Jason Staten <jstaten@peer60.com>  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure
locales  
  
RUN apt-get update && apt-get -y --force-yes install wget  
  
ADD sources.list /etc/apt/sources.list.d/peer60-postgres.list  
  
RUN wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc |
apt-key add -  
  
RUN apt-get update --no-list-cleanup\  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install
postgresql-9.3 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
ADD pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
ADD postgresql.conf /etc/postgresql/9.3/main/postgresql.conf  
  
USER postgres  
  
EXPOSE 5432  
CMD /usr/lib/postgresql/9.3/bin/postgres -D \  
/var/lib/postgresql/9.3/main -c \  
config_file=/etc/postgresql/9.3/main/postgresql.conf  

