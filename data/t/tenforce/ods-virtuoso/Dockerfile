FROM nicholsn/virtuoso  
ADD virtuoso.ini /var/lib/virtuoso/db/  
ADD http://data.opendatasupport.eu/data.tgz /var/lib/virtuoso/db/  
RUN cd /var/lib/virtuoso/db && virtuoso-t +wait && tar xzf data.tgz && echo
"ld_dir('/var/lib/virtuoso/db/data', '*.ttl',
NULL);\nrdf_loader_run();\nexec('checkpoint');\nshutdown();" | isql-v -U dba
-P dba  

