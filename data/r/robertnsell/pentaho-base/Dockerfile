FROM openjdk:latest  
  
# Install OpenJDK JRE  
# RUN apt-get upgrade && apt-get update  
# RUN add-apt-repository ppa:openjdk-r/ppa && apt-get update && apt-get
install openjdk-7-jdk  
# RUN pt-get download libwebkitgtk-1.0-0  
# Set environment variables for Java JRE and Pentaho  
# ENV JAVA_HOME=/usr/lib/jvm/default-jvm/jre  
# ENV JRE_HOME=${JAVA_HOME} \  
# PENTAHO_JAVA_HOME=${JAVA_HOME} \  
RUN apt-get update && apt-get install  
  
ENV DEST_DIR=/home/pentaho \  
ARCHIVE_FILE=pdi-ce-7.0.0.0-25.zip \  
PENTAHO_HOME=${DEST_DIR}/data-integration \  
PENTAHO_USERNAME=pentaho  
# PATH=${PATH}:${JAVA_HOME}/bin:${JRE_HOME}/bin  
# Add a user (user id 500) with no login and create the pentaho home
directory.  
RUN adduser -h ${DEST_DIR} -s /bin/false -D -u 555 ${PENTAHO_USERNAME}  
  
WORKDIR ${DEST_DIR}  
  
# Get and unpack pdi-ce 6.0 stable.  
# COPY pdi-ce-7.0.0.0-25.zip pdi-ce-7.0.0.0-25.zip  
RUN wget
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/7.0/${ARCHIVE_FILE}
\  
&& unzip ${ARCHIVE_FILE} \  
&& rm -f ${ARCHIVE_FILE} \  
&& chown -R 555 /home/pentaho/data-integration/  

