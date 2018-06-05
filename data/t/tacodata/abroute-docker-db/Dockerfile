#  
# this container is used for two things.  
# abinit will create a new database and prime it with data to get started  
# absql will run a database server (you should mount a database created with
abinit)  
#  
FROM tacodata/abroute-docker-base  
  
MAINTAINER Greg Fausak <greg@tacodata.com>  
  
RUN pip install web.py  
  
COPY PG.sql /usr/local/etc/  
COPY abinit abadm.py /usr/local/bin/  
  
VOLUME ["/var/lib/postgresql"]  
VOLUME ["/etc/postgresql"]  
VOLUME ["/run/postgresql"]  
  
ENTRYPOINT ["abinit"]  

