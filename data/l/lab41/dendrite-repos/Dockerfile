FROM lab41/dendrite-snap  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
ENV REPOS_PULLED 07-15-2014  
RUN git clone https://github.com/Lab41/titan.git  
RUN cd /titan; git checkout dendrite-hadoop2  
RUN mvn -Dmaven.repo.local=/root/lib install -f /titan/pom.xml -DskipTests; \  
rm -rf /titan  
RUN git clone https://github.com/Lab41/faunus.git  
RUN cd /faunus; git checkout dendrite-hadoop2  
RUN mvn -Dmaven.repo.local=/root/lib install -f /faunus/pom.xml -DskipTests  
RUN git clone https://github.com/Lab41/incubator-twill.git  
RUN cd incubator-twill; git checkout sync  
RUN mvn -Dmaven.repo.local=/root/lib install -f /incubator-twill/pom.xml
-DskipTests; \  
rm -rf /incubator-twill  
RUN git clone https://github.com/Lab41/graphlab-twill.git  
RUN cd /graphlab-twill; git checkout master  
RUN mvn -Dmaven.repo.local=/root/lib install -f /graphlab-twill/pom.xml
-DskipTests  
  
ENV DENDRITE_PULLED 07-15-2014  
RUN git clone https://github.com/Lab41/Dendrite.git  
  
RUN sed 's|<connectionUrl>scm:git:git@github.com:kylef-
lab41/ungit.git</connectionUrl>|<connectionUrl>scm:git:https://github.com/kylef-
lab41/ungit.git</connectionUrl>|' -i /Dendrite/pom.xml; \  
sed 's|cluster-size=2|cluster-size=1|' -i /Dendrite/src/main/webapp/WEB-
INF/prod/graphlab.properties; \  
sed
's|~/graphlab/release/toolkits/graph_analytics/|/usr/share/tomcat7/graphlab/release/toolkits/graph_analytics|'
-i /Dendrite/src/main/webapp/WEB-INF/prod/graphlab.properties  
  
RUN cd /Dendrite; mvn scm:checkout -DwithGitHistoryServer=true  
RUN sed 's/user: <FIXME.*>/user: "lab41"/' -i
/Dendrite/src/main/nodejs/ungit/public/source/app.js; \  
sed 's|local: <FIXME.*>|local: "/tmp/dendrite/history"|' -i
/Dendrite/src/main/nodejs/ungit/public/source/app.js; \  
sed 's|remote: <FIXME.*>|remote: "https://github.com"|' -i
/Dendrite/src/main/nodejs/ungit/public/source/app.js; \  
sed -i "s/port:.*/port: parseInt(window.location.port)+1,/g"
/Dendrite/src/main/webapp/js/app.js; \  
sed -i "s/host:.*/host: window.location.hostname,/g"
/Dendrite/src/main/webapp/js/app.js  
RUN npm install less  
RUN service hadoop-hdfs-namenode start; \  
service hadoop-hdfs-datanode start; \  
sleep 30; \  
hadoop fs -put /Dendrite/src/main/groovy/org/lab41/dendrite/dendrite-
import.groovy /user/root/dendrite/dendrite-import.groovy  

