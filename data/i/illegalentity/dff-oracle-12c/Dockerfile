FROM sath89/oracle-12c-base  
MAINTAINER Daevid Preis <daevid.preis@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y git  
  
ENV WEB_CONSOLE ""  
ENV DBCA_TOTAL_MEMORY 1024  
ENV ORACLE_USER oracle  
  
EXPOSE 1521  
EXPOSE 8080  
VOLUME ["/u01/app/oracle"]  
VOLUME ["/import.d"]  
  
ADD setup /setup  
ADD import /import  
ADD migrate-db /migrate-db  
ADD utils/colors /utils/colors  
RUN chmod +x /setup /import /migrate-db  
  
ENTRYPOINT ["/setup"]  
CMD [""]  

