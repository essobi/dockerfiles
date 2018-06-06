FROM solr:6.6.2  
RUN curl -Ls
'https://search.maven.org/remotecontent?filepath=com/vividsolutions/jts/1.13/jts-1.13.jar'
-o '/opt/solr/server/solr-webapp/webapp/WEB-INF/lib/jts-1.13.jar' \  
&& curl -Ls
"http://artifacts.codice.org/service/local/artifact/maven/content?r=snapshots&g=ddf.platform.solr&a=solr-
xpath&v=2.11.3-SNAPSHOT" -o '/opt/solr/server/solr-webapp/webapp/WEB-
INF/lib/solr-xpath-2.11.3-SNAPSHOT.jar'  

