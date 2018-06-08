#  
# DCM4CHEE - Open source picture archive and communications server (PACS)  
#  
FROM ubuntu:14.04  
ENV DCM_ARC_VERSION=2.18.0  
ENV DCM_ARR_VERSION=3.0.11  
ENV DCM4CHEE_HOME=/var/local/dcm4chee  
  
RUN mkdir -p ${DCM4CHEE_HOME}  
  
WORKDIR ${DCM4CHEE_HOME}  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
wget zip unzip openjdk-6-jdk python mysql-server  
  
# Download the binary package for DCM4CHEE  
RUN wget -q
http://downloads.sourceforge.net/project/dcm4che/dcm4chee/${DCM_ARC_VERSION}/dcm4chee-${DCM_ARC_VERSION}-mysql.zip
\  
-O /tmp/dcm4chee-${DCM_ARC_VERSION}-mysql.zip  
RUN unzip -q /tmp/dcm4chee-${DCM_ARC_VERSION}-mysql.zip -d ${DCM4CHEE_HOME}  
ENV DCM_DIR=${DCM4CHEE_HOME}/dcm4chee-${DCM_ARC_VERSION}-mysql  
  
  
# Download the binary package for JBoss  
RUN wget -q
http://downloads.sourceforge.net/project/jboss/JBoss/JBoss-4.2.3.GA/jboss-4.2.3.GA-
jdk6.zip \  
-O /tmp/jboss-4.2.3.GA-jdk6.zip  
RUN unzip -q /tmp/jboss-4.2.3.GA-jdk6.zip -d ${DCM4CHEE_HOME}  
ENV JBOSS_DIR=${DCM4CHEE_HOME}/jboss-4.2.3.GA  
  
  
# Download the Audit Record Repository (ARR) package  
RUN wget -q http://downloads.sourceforge.net/project/dcm4che/dcm4chee-
arr/${DCM_ARR_VERSION}/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip \  
-O /tmp/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip  
RUN unzip -q /tmp/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip -d
${DCM4CHEE_HOME}  
ENV ARR_DIR ${DCM4CHEE_HOME}/dcm4chee-arr-${DCM_ARR_VERSION}-mysql  
  
  
# Copy files from JBoss to dcm4chee  
RUN ${DCM_DIR}/bin/install_jboss.sh ${JBOSS_DIR} > /dev/null  
# Copy files from the Audit Record Repository (ARR) to dcm4chee  
RUN ${DCM_DIR}/bin/install_arr.sh ${ARR_DIR} > /dev/null  
  
# Patch the JPEGImageEncoder issue for the WADO service  
RUN sed -e
"s/value=\"com.sun.media.imageioimpl.plugins.jpeg.CLibJPEGImageWriter\"/value=\"com.sun.image.codec.jpeg.JPEGImageEncoder\"/g"
\  
< $DCM_DIR/server/default/conf/xmdesc/dcm4chee-wado-xmbean.xml > dcm4chee-
wado-xmbean.xml && \  
mv dcm4chee-wado-xmbean.xml $DCM_DIR/server/default/conf/xmdesc/dcm4chee-wado-
xmbean.xml  
  
# Update environment variables  
RUN echo "\  
JAVA_HOME=/usr/lib/jvm/java-6-openjdk-amd64\n\  
PATH=\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"\n\  
" > /etc/environment  
  
# Load the stage folder, which contains the setup scripts.  
ADD stage stage  
RUN chmod 755 stage/*.bash  
RUN cd stage; ./setup_mysql.bash  
  
# DICOM port  
EXPOSE 11112  
# HL7 port  
EXPOSE 2575  
# DCM4CHEE webapp  
EXPOSE 8080  
CMD ["stage/start.bash"]  

