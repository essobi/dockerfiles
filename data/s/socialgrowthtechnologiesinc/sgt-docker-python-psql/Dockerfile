FROM socialgrowthtechnologiesinc/sgt-docker-python:latest  
MAINTAINER djfatchuck "charles.schrumpf@gmail.com"  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update  
RUN apt-get install -y language-pack-en  
RUN apt-get install -y postgresql-9.4  
RUN sed -i 's/peer/trust/' /etc/postgresql/9.4/main/pg_hba.conf  
RUN sed -i 's/md5/trust/' /etc/postgresql/9.4/main/pg_hba.conf  

