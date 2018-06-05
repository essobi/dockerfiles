FROM ancine/jbpm  
  
ENV SRC_DIR=/opt/jboss/src  
ENV DATA_DIR /opt/jboss/data  
  
ENV
KIE_SERVER_WAR_URL=http://repository.jboss.org/nexus/content/groups/public-
jboss/org/kie/server/kie-server/7.3.0.Final/kie-server-7.3.0.Final-ee7.war  
ENV CASE_MGMT_WAR_URL=http://repository.jboss.org/nexus/content/groups/public-
jboss/org/jbpm/jbpm-wb-case-mgmt-showcase/7.3.0.Final/jbpm-wb-case-mgmt-
showcase-7.3.0.Final-wildfly10.war  
  
  
ENV JAVA_OPTS -Xms512m -Xmx2000m -Djava.net.preferIPv4Stack=true  
  
  
USER jboss  
RUN mkdir -p $SRC_DIR $DATA_DIR  
  
COPY support/standalone-full.xml $JBOSS_HOME/standalone/configuration/  
  
USER root  
RUN yum install -y git \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& curl -sSL
http://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-3.2.5 /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& mkdir /opt/jboss/.m2 \  
&& chown -R jboss:jboss $JBOSS_HOME/standalone/configuration/standalone-
full.xml \  
/opt/jboss/.m2 \  
$DATA_DIR  
USER jboss  
  
RUN curl -J -L $KIE_SERVER_WAR_URL -o
/opt/jboss/wildfly/standalone/deployments/kie-server.war \  
&& curl -J -L $CASE_MGMT_WAR_URL -o
/opt/jboss/wildfly/standalone/deployments/jbpm-casemgmt.war  
  
RUN $JBOSS_HOME/bin/add-user.sh -u admin -p ancine1! --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u admin -p ancine1! -ro
analyst,admin,user,manager,kiemgmt,kie-server,rest-
all,SIM_PROPONENTE,SIM_COORD_TRIAGEM,SIM_COORD_ANALISE_DIREITOS,SIM_COORD_ANALISE_TECNICA,SIM_SUP_FOMENTO
--silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u kiecontrolleruser -p
kiecontrolleruser1! -ro kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u proponente.user.1 -p
ancine1! -ro SIM_PROPONENTE,user --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u proponente.user.2 -p
ancine1! -ro SIM_PROPONENTE,user --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u coord.triagem.1 -p
ancine1! -ro SIM_COORD_TRIAGEM,user,manager --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u coord.triagem.2 -p
ancine1! -ro SIM_COORD_TRIAGEM,user,manager --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u
coord.analise.direitos.1 -p ancine1! -ro
SIM_COORD_ANALISE_DIREITOS,user,manager --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u
coord.analise.direitos.2 -p ancine1! -ro
SIM_COORD_ANALISE_DIREITOS,user,manager --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u
coord.analise.tecnica.1 -p ancine1! -ro SIM_COORD_ANALISE_TECNICA,user,manager
--silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u
coord.analise.tecnica.2 -p ancine1! -ro SIM_COORD_ANALISE_TECNICA,user,manager
--silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u sup.fomento -p
ancine1! -ro SIM_SUP_FOMENTO,user,manager --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u krisv -p krisv -ro
admin,analyst,kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u john -p john -ro
analyst,Accounting,PM,kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u sales-rep -p sales-
rep -ro analyst,sales,kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u katy -p katy -ro
analyst,HR,kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u jack -p jack -ro
analyst,IT,kie-server,rest-all --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u maciek -p maciek1!
-ro employees,kie-server,rest-all,user,IT --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u tihomir -p tihomir1!
-ro employees,apple,dell,lenovo,other,kie-server,rest-all,user,IT --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u krisv -p krisv1! -ro
employees,manager,kie-server,rest-all,user,IT --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u mary -p mary1! -ro
employees,manager,kie-server,rest-all,user,IT --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u paul -p paul1! -ro
employees,manager,kie-server,rest-all,user,IT --silent \  
&& $JBOSS_HOME/bin/add-user.sh -a -r ApplicationRealm -u kieserver -p
kieserver1! -ro employees,kie-server,rest-all,user --silent  
  
  
VOLUME $DATA_DIR  
VOLUME /opt/jboss/.m2  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-c", "standalone-full.xml",
"-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]  

