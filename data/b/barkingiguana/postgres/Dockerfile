FROM barkingiguana/base  
  
MAINTAINER Craig R Webster <craig@barkingiguana.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq postgresql-server-
dev-9.3 postgresql-9.3 postgresql-contrib-9.3  
ADD ./pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf  
ADD ./postgresql.conf /etc/postgresql/9.3/main/postgresql.conf  
ADD ./start-postgres.sh /usr/sbin/start-postgres  
RUN chmod +x /usr/sbin/start-postgres  
RUN chown postgres:postgres /var/lib/postgresql/9.3/main/base  
  
EXPOSE 5432  
CMD [ "/usr/sbin/start-postgres" ]  

