FROM percona/percona-xtradb-cluster:5.6.36  
# cleanup  
RUN rm -f \  
/usr/bin/clustercheckcron \  
/percona-release_0.1-4.jessie_all.deb \  
/entrypoint.sh  
  
# dumb-init  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
COPY readiness_probe.sh /usr/local/bin/  
  
COPY wsrep_sst_mysqldump_nc /usr/bin/  
RUN chmod a+x /usr/bin/wsrep_sst_mysqldump_nc  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

