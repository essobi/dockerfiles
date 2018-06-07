FROM tutum/jboss:as7  
MAINTAINER Michal Rus <m@michalrus.com>  
  
ENV DROOLS_VERSION 5.5.0.Final  
  
RUN apt-get update && \  
apt-get install -y unzip && \  
wget http://download.jboss.org/drools/release/${DROOLS_VERSION}/guvnor-
distribution-${DROOLS_VERSION}.zip -O /tmp/guvnor-
distribution-${DROOLS_VERSION}.zip && \  
unzip -q /tmp/guvnor-distribution-${DROOLS_VERSION}.zip -d /tmp/ && \  
chown -R 501:501 /tmp/guvnor-distribution-${DROOLS_VERSION}/ && \  
cd /jboss-as-7.*/standalone/deployments/ && \  
mv /tmp/guvnor-
distribution-${DROOLS_VERSION}/binaries/guvnor-${DROOLS_VERSION}-jboss-
as-7.*.war ./drools-guvnor.war && \  
cd / && \  
rm -rf /tmp/* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/run.sh"]  

