FROM pataquets/solr:4.10.4  
ADD files/entrypoint.sh /entrypoint.sh  
ADD files/etc/default/solr /etc/default/solr  
ADD files/opt/solr/example/solr/collection1/conf
/opt/solr/example/solr/collection1/conf/  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

