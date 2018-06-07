FROM sath89/oracle-12c-base  
  
### This image is a build from non automated image cause of no possibility of
Oracle 12c instalation in Docker container  
ENV WEB_CONSOLE true  
ENV DBCA_TOTAL_MEMORY 1024  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/u01/app/oracle/product/12.1.0/xe/bin  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN echo "deb http://de.archive.ubuntu.com/ubuntu xenial main restricted
universe multiverse" >> /etc/apt/sources.list  
RUN apt-get update && apt-get install -y wget && apt-get clean && rm -rf
/tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
# add sample data  
RUN sh -c "wget 'https://s3.amazonaws.com/sequelize/data.tar.gz' && \  
sudo tar xf data.tar.gz -C /u01/app/oracle && \  
sudo chmod -R +rw /u01/app/oracle"  
  
EXPOSE 1521  
EXPOSE 5500  
VOLUME ["/docker-entrypoint-initdb.d"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

