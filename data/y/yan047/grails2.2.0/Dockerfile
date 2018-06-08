# Version: 1  
# Name: jdk6  
FROM yan047/jdk6:1  
MAINTAINER "boyan.au@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# In case someone loses the Dockerfile  
RUN rm -rf /etc/Dockerfile  
ADD Dockerfile /etc/Dockerfile  
  
# Create needed directories  
ENV DOWNLOAD_DIR /srv/downloads  
RUN mkdir -p "${DOWNLOAD_DIR}"  
  
# Install Grails  
WORKDIR ${DOWNLOAD_DIR}  
ENV GRAILS_VERSION=grails-2.2.0  
ENV GRAILS_FILE=${GRAILS_VERSION}.zip  
  
RUN wget
http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/${GRAILS_FILE}
&& \  
unzip ${GRAILS_FILE} && \  
rm -rf ${GRAILS_FILE} && \  
mv ${GRAILS_VERSION} /opt && \  
ln -s /opt/${GRAILS_VERSION} /opt/grails && \  
rm -rf ${DOWNLOAD_DIR}* && rm -rf /var/log/*  
  
ENV GRAILS_HOME /opt/grails  
ENV PATH $GRAILS_HOME/bin:$PATH

