#start with elastic as base  
FROM mariusspielberger/se-project-base:latest  
  
USER root  
  
ADD config/elasticsearch.yml /usr/share/elasticsearch/config  
ADD config/logstash.yml /usr/share/elasticsearch/config/  
ADD config/kibana.yml /usr/share/elasticsearch/config/  
ADD config/log4j.properties /usr/share/elasticsearch/config/  
ADD config/jvm.options /usr/share/elasticsearch/config/  
ADD config/logstash-twitter.conf /usr/share/elasticsearch/pipeline/  
RUN mkdir -p /usr/share/elasticsearch/node_modules/node-red-contrib-mapauth  
ADD config/map-auth.html /usr/share/elasticsearch/node_modules/node-red-
contrib-mapauth/  
ADD config/map-auth.js /usr/share/elasticsearch/node_modules/node-red-contrib-
mapauth/  
ADD config/package.json /usr/share/elasticsearch/node_modules/node-red-
contrib-mapauth/  
RUN mkdir -p /usr/share/elasticsearch/.node-red  
ADD config/flows_se-project.json /usr/share/elasticsearch/.node-red  
RUN chown elasticsearch: /usr/share/elasticsearch/.node-red/  
RUN chown elasticsearch: /usr/share/elasticsearch/node_modules/  
  
#copy startup script  
ADD startup.sh /usr/share/elasticsearch/  
  
RUN cd /usr/share/elasticsearch/node_modules/node-red && npm install node-red-
node-geohash@0.0.7  
  
#add snapshot data  
ADD snapshots /usr/share/elasticsearch/snapshots  
  
RUN chown --recursive elasticsearch:elasticsearch
/usr/share/elasticsearch/config/ /usr/share/elasticsearch/pipeline/
/usr/share/elasticsearch/node_modules/node-red/node_modules
/usr/share/elasticsearch/snapshots  
RUN chmod 0777 startup.sh  
  
#becasue elastic starts whining if started as root  
USER elasticsearch  
  
#bring up elastic and import the snapshot data && and delete snapshot from
repo  
RUN echo 'Run elastic' && elasticsearch & echo 'Wait for it to start' && sleep
60s && echo 'make repo known' && curl -H 'Content-Type:application/json' -d
'{"type":"fs","settings":{"compress":true,"location":"repo"}}' -X PUT
localhost:9200/_snapshot/repo && sleep 10s && echo 'restore backup' && curl -X
POST localhost:9200/_snapshot/repo/snap/_restore && echo 'wait for it to
finish properly' && sleep 60s && echo 'delet snapshot' && curl -X DELETE
localhost:9200/_snapshot/repo/snap && sleep 10s  
  
#elastic gets killed as the bash dies; so no work for us here :)  
EXPOSE 9500 9600 9200 9300 5601 1880  
CMD ["/bin/bash", "/usr/share/elasticsearch/startup.sh"]  

