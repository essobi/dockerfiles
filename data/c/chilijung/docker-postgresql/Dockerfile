FROM ubuntu  
MAINTAINER chilijung <chilijung@gmail.com>  
  
# Exposes  
EXPOSE 5432  
# Credentials  
ENV USERNAME docker  
ENV PASS d0cker  
  
RUN apt-get install -y curl wget  
  
RUN touch /etc/apt/sources.list.d/pgdg.list  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list  
  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
# Update the package repository  
RUN apt-get update  
RUN apt-get install -y postgresql-9.3  
  
# add postgresql configure files  
ADD pg_hba.conf /etc/postgresql/9.3/main/  
ADD pg_ident.conf /etc/postgresql/9.3/main/  
ADD postgresql.conf /etc/postgresql/9.3/main/  
  
# main entry  
ADD start /start  
RUN chmod 0755 /start  
  
# restart service  
CMD ["/start"]  
  
RUN service postgresql restart  

