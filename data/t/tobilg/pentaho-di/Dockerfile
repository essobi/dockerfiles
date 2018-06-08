FROM java:8-jre  
  
MAINTAINER TobiLG <tobilg@gmail.com>  
  
# https://sourceforge.net/projects/pentaho/files/Data%20Integration/6.1/pdi-
ce-6.1.0.1-196.zip/download  
# Set required environment vars  
ENV PDI_RELEASE=6.1 \  
PDI_VERSION=6.1.0.1-196 \  
CARTE_PORT=8181 \  
PENTAHO_JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \  
PENTAHO_HOME=/home/pentaho  
  
# Create user  
RUN mkdir ${PENTAHO_HOME} && \  
groupadd -r pentaho && \  
useradd -s /bin/bash -d ${PENTAHO_HOME} -r -g pentaho pentaho && \  
chown pentaho:pentaho ${PENTAHO_HOME} && \  
mkdir -p $PENTAHO_HOME/docker-entrypoint.d $PENTAHO_HOME/templates
$PENTAHO_HOME/scripts && \  
curl -sSL https://raw.githubusercontent.com/tobilg/mesosdns-
resolver/master/mesosdns-resolver.sh -o /usr/local/bin/mesosdns-resolver && \  
chmod +x /usr/local/bin/mesosdns-resolver && \  
apt-get update && \  
apt-get install -y dnsutils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN chown -R pentaho:pentaho $PENTAHO_HOME  
  
# Switch to the pentaho user  
USER pentaho  
  
# Download PDI  
RUN /usr/bin/wget \  
\--progress=dot:giga \  
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/${PDI_RELEASE}/pdi-
ce-${PDI_VERSION}.zip \  
-O /tmp/pdi-ce-${PDI_VERSION}.zip && \  
/usr/bin/unzip -q /tmp/pdi-ce-${PDI_VERSION}.zip -d $PENTAHO_HOME && \  
rm /tmp/pdi-ce-${PDI_VERSION}.zip  
  
# We can only add KETTLE_HOME to the PATH variable now  
# as the path gets eveluated - so it must already exist  
ENV KETTLE_HOME=$PENTAHO_HOME/data-integration \  
PATH=$KETTLE_HOME:$PATH  
  
COPY carte-*.config.xml $PENTAHO_HOME/templates/  
  
COPY entrypoint.sh $PENTAHO_HOME/scripts/  
  
# Expose Carte Server  
EXPOSE ${CARTE_PORT}  
  
# As we cannot use env variable with the entrypoint and cmd instructions  
# we set the working directory here to a convenient location  
# We set it to KETTLE_HOME so we can start carte easily  
WORKDIR $KETTLE_HOME  
  
ENTRYPOINT ["../scripts/entrypoint.sh"]  
  
# Run Carte - these parameters are passed to the entrypoint  
#CMD ["carte.sh", "carte.config.xml"]  

