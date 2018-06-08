FROM java:7  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64\  
PROFILE=\  
MOUNT_REGISTRY=false\  
WELL_KNOWN_ADDRESSES=  
  
# Copy all the custom files to /files  
COPY files /files  
  
  
# This is the pre-packaged identity server 5.0.0 with api manager 1.9.1  
# Came from https://docs.wso2.com/display/CLUSTER420/Configuring+the+Pre-
Packaged+Identity+Server+5.0.0+with+API+Manager+1.9.1  
  
RUN echo 'deb http://http.us.debian.org/debian squeeze main' >
/etc/apt/sources.list.d/squeeze.list && \  
apt-get update && \  
apt-get install --force-yes -y zip xmlstarlet libsvn1=1.6.12dfsg-7
subversion=1.6.12dfsg-7 && \  
apt-get autoremove -y && \  
apt-get clean && \  
wget -P /opt/ http://product-dist.wso2.com/downloads/api-
manager/1.9.1/identity-server/wso2is-5.0.0.zip && \  
rm /etc/apt/sources.list.d/squeeze.list && \  
unzip /opt/wso2is-5.0.0.zip -d /opt && \  
mv /opt/wso2is-5.0.0 /opt/wso2 && \  
rm /opt/wso2is-5.0.0.zip && \  
wget -P /opt/wso2/repository/components/lib/
https://jdbc.postgresql.org/download/postgresql-9.4-1203.jdbc41.jar && \  
wget -P /opt/wso2/repository/components/dropins/
http://dist.wso2.org/tools/svnkit-1.3.9.wso2v2.jar && \  
wget -P /opt/wso2/repository/components/lib/
http://maven.wso2.org/nexus/content/groups/wso2-public/com/trilead/trilead-
ssh2/1.0.0-build215/trilead-ssh2-1.0.0-build215.jar && \  
  
# Overlay /files onto /opt/wso2  
cp -R /files/* /opt/wso2/ && \  
chmod a+x /opt/wso2/bin/*.sh && \  
  
# Download the property parser (to convert a properties file into property
arguments)  
wget -O /opt/wso2/bin/property-parser.jar
https://github.com/MashupMill/property-parser/releases/download/1.6/property-
parser-1.6.jar  
  
# Define a volume where people can mount custom files to override anything in
the wso2 product  
VOLUME ["/extra", "/startup.d"]  
WORKDIR /opt/wso2/  
EXPOSE 9443 9763  
CMD ["/opt/wso2/bin/entrypoint.sh"]  

