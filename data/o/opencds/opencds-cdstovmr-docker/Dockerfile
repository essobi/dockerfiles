# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER Salvador Rodriguez <salvador.rodriguez@utah.edu>  
  
# Install packages  
ENV REFRESHED_AT 2015-07-20  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install wget pwgen unzip software-properties-common ca-
certificates sqlite3 libsqlite3-dev libdbd-sqlite3-perl libtext-csv-perl
mercurial expect && \  
wget download.java.net/glassfish/3.1.2/release/glassfish-3.1.2.zip && \  
# The CDA redaction web service does not work with glassfish version 4,
version 3.1.2 is the recommended version  
unzip glassfish-3.1.2.zip -d /opt && \  
rm glassfish-3.1.2.zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# get maven 3.2.2  
RUN wget --no-verbose -O /tmp/apache-maven-3.2.2.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.2.2/binaries/apache-
maven-3.2.2-bin.tar.gz  
  
# verify checksum  
RUN echo "87e5cc81bc4ab9b83986b3e77e6b3095 /tmp/apache-maven-3.2.2.tar.gz" |
md5sum -c  
  
# install maven  
RUN tar xzf /tmp/apache-maven-3.2.2.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.2.2 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.2.2.tar.gz  
ENV MAVEN_HOME /opt/maven  
RUN echo export M2_HOME=/usr/share/maven >> ~/.bashrc  
  
ENV PATH /opt/glassfish3/bin:$PATH  
ENV GLASSFISH /opt/glassfish3/  
  
# ssh  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# Install Java (important to used java 7, it did not work with version 8)  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
RUN echo PATH=$JAVA_HOME/bin:$PATH:$HOME/bin >> ~/.bashrc  
RUN echo export PATH JAVA_HOME >> ~/.bashrc  
  
# DS2 HOME  
ENV DS2_HOME /ds2  
RUN mkdir ${DS2_HOME}  
WORKDIR ${DS2_HOME}  
  
########################################################################################  
# CCD-to-vMR conversion requires:  
# - CDA Web Service (also known as "CDA Redaction Web Service")  
# - CDA Predicate Reducer Web App for a web browser-based front-end to the
service  
########################################################################################  
# mvn clean install did not work on this project, docker issues when
downloading stuff from the web  
#RUN hg clone https://bitbucket.org/sharps-ds2/cda-web-service  
#COPY ejb-jar.xml cda-web-service/cda-ws-ejb/src/main/resources/META-INF/  
#RUN cd cda-web-service; mvn clean install  
COPY reducer-env.properties $GLASSFISH/glassfish/domains/domain1/config/  
RUN mkdir /tmp/cda-ws  
COPY cda-ws-ear.ear /tmp/cda-ws/  
COPY ejb-jar.xml /tmp/cda-ws/  
RUN cd /tmp/cda-ws/; unzip cda-ws-ear.ear && \  
rm cda-ws-ear.ear && \  
unzip cda-ws-ejb.jar -d cda-ws-ejb/ && \  
rm cda-ws-ejb.jar; rm cda-ws-ejb/META-INF/ejb-jar.xml && \  
mv ejb-jar.xml cda-ws-ejb/META-INF/ && \  
jar cf cda-ws-ejb.jar -C cda-ws-ejb . && \  
rm -rf cda-ws-ejb/ && \  
jar cf cda-ws-ear.ear *  
RUN mv /tmp/cda-ws/cda-ws-ear.ear
$GLASSFISH/glassfish/domains/domain1/autodeploy/; rm -rf /tmp/cda-ws/  
COPY cda-ws-web.war $GLASSFISH/glassfish/domains/domain1/autodeploy/  
  
########################################################################################  
# CCD redaction via web service-deterministic rules requires:  
# - DS2 Data Scripts  
# - NaiveBayesPredicate  
# - Predicate/Reducer  
# - CDA Web Service (also known as "CDA Redaction Web Service")  
# - CDA Predicate Reducer Web App for a web browser-based front-end to the
service  
# - CAT CDA Plug-in (including the CDA MTS Service and CDA CAT Web
Application) for an optional web-based test manager  
########################################################################################  
# DS2 Data Scripts  
RUN hg clone https://bitbucket.org/sharps-ds2/ds2_data_scripts  
  
# The following script will pull down public available datasets necessary for
DTS2 (e.g., ICD9 codes, hospital discharge, public datasets, etc)  
# once the data is downloaded it will parce the data, load it into the
database and generate statistics for the application  
RUN cd ds2_data_scripts; yes Y | sh ./quickstart.sh custom_hiv_concepts  
  
# NaiveBayesPredicate  
RUN hg clone https://bitbucket.org/sharps-ds2/naivebayespredicate  
COPY naivebayespredicate.properties
naivebayespredicate/src/main/resources/org/sharps/ds2/predicate/  
RUN cd naivebayespredicate; mvn clean install -Dmaven.compiler.source=1.7
-Dmaven.compiler.target=1.7  
  
########################################################################################  
# Web-based CCD editing requires:  
# - Predicate/Reducer  
# - CDA Web Service (also known as "CDA Redaction Web Service")  
# - CDA Predicate Reducer Web App for a web browser-based front-end to the
service  
# - CAT CDA Plug-in (including the CDA MTS Service and CDA CAT Web
Application) for an optional web-based test manager  
########################################################################################  
# Predicate/Reducer  
RUN hg clone https://bitbucket.org/sharps-ds2/predicate-reducer  
COPY log4j.properties predicate-reducer/opencds/opencds-parent/opencds-
decision-support-service/src/main/resources/  
COPY opencds-decision-support-service-config.xml predicate-
reducer/opencds/opencds-parent/opencds-decision-support-
service/src/main/resources/  
  
COPY tls_Icd10HumanReadableMap_INT_20131220.tsv data/  
COPY SNOMEDCT_CORE_SUBSET_201311.txt data/  
COPY ICD9CM_SNOMED_MAP_1TO1.txt data/  
COPY ICD9CM_SNOMED_MAP_1TOM.txt data/  
COPY opencds_concept_generator.sh ds2_data_scripts/  
RUN cd ds2_data_scripts; sh ./opencds_concept_generator.sh  
  
RUN cd predicate-reducer/opencds/opencds-parent; mvn clean install  
RUN cd predicate-reducer/opencds/opencds-parent/opencds-decision-support-
service; mvn clean install  
  
RUN cp predicate-reducer/opencds/opencds-parent/opencds-decision-support-
service/target/opencds-decision-support-service-1.2.0-SNAPSHOT.war
$GLASSFISH/glassfish/domains/domain1/autodeploy/  
  
# mts-ear-cda & cat-cda  
# TODO  
#RUN hg clone https://bitbucket.org/sharps-ds2/cdsframework-cda-service  
#RUN cd cdsframework-cda-service; mvn clean install  
#RUN cp cdsframework-cda-service/mts-ear-cda/target/mts.ear
$GLASSFISH/glassfish/domains/domain1/autodeploy/  
#RUN cp cdsframework-cda-service/cat-cda/target/cat.war
$GLASSFISH/glassfish/domains/domain1/autodeploy/  
#COPY mts.ear $GLASSFISH/glassfish/domains/domain1/autodeploy/  
#COPY cat.war $GLASSFISH/glassfish/domains/domain1/autodeploy/  
########################################################################################  
# HIE Prototype with all of the above  
# - Install everything for CCD redaction via web service - with probabilistic
rules (Test Manager not required)  
# - Then install the HIE Prototype project  
########################################################################################  
# TODO  
########################################################################################  
# Inference Analyzer only:  
# - DS2 Data Scripts  
# - NaiveBayesPredicate  
# - RandomForestPredicate  
# - Inference Analyzer  
########################################################################################  
# RandomForestPredicate  
RUN hg clone https://bitbucket.org/sharps-ds2/randomforestpredicate  
RUN cd randomforestpredicate; mvn clean install  
  
# Inference Analyzer  
RUN hg clone https://bitbucket.org/sharps-ds2/simplepredicatereducervisualizer  
RUN cd simplepredicatereducervisualizer; mvn clean install  
RUN cp
simplepredicatereducervisualizer/target/SimplePredicateReducerVisualizer-1.0-SNAPSHOT.war
$GLASSFISH/glassfish/domains/domain1/autodeploy/  
  
########################################################################################  
# Classifier development and testing  
# - DS2 Data Scripts  
# - WEKA (see Software Used by DS2)  
########################################################################################  
# TODO  
# Add image scripts  
COPY run.sh ./  
COPY change_admin_password.sh ./  
COPY change_admin_password_func.sh ./  
COPY enable_secure_admin.sh ./  
RUN chmod +x *.sh  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener), 22 (ssh)  
EXPOSE 4848 8080 8181 22  
# 9009 (debug port)  
EXPOSE 9009  
CMD ["/run.sh"]  

