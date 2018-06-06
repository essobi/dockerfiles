FROM klaemo/couchdb:latest  
MAINTAINER Michael Yuen <michael.yuen@mac.com>  
  
EXPOSE 5984 5986 4369  
COPY local.ini /opt/couchdb/etc/local.ini  
COPY vm.args.template /opt/couchdb/etc/vm.args.template  
  
COPY scripts/couchdb-register.sh /usr/bin/couchdb-register.sh  
COPY scripts/couchdb-cluster-setup.sh /usr/bin/couchdb-cluster-setup.sh  
COPY scripts/couchdb-cluster-finish.sh /usr/bin/couchdb-cluster-finish.sh  
  
COPY scripts/couchdb-entrypoint.sh /usr/bin/couchdb-entrypoint.sh  
  
ENTRYPOINT ["tini", "--", "/usr/bin/couchdb-entrypoint.sh"]  
  
CMD ["/opt/couchdb/bin/couchdb"]  

