FROM debian:jessie  
  
RUN apt-get update  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >>
/etc/apt/sources.list  
RUN apt-get install -y wget ca-certificates  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update  
#RUN apt-get upgrade  
RUN apt-get install -y postgresql-9.4 pgadmin3  
RUN apt-get install -y libpq-dev sqitch

