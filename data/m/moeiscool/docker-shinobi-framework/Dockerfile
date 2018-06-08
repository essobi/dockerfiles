FROM ubuntu:artful  
  
#make working directory  
RUN mkdir /opt/sql  
WORKDIR /opt/sql  
  
#get apt list  
RUN apt update -y  
  
#MariaDB Install  
COPY shinobi-framework.sql .  
RUN apt install mariadb-server mariadb-client -y  
RUN mysql -e "source /opt/sql/shinobi-framework.sql" || true  
  
#create entrypoint file  
COPY docker-entrypoint.sh .  
RUN chmod -f +x ./*.sh  
  
#default SQL port  
EXPOSE 3306  
#run docker  
ENTRYPOINT ["/opt/sql/docker-entrypoint.sh" ]

