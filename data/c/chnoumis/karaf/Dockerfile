FROM fabric8/s2i-karaf:1.2.5  
MAINTAINER chnoumis  
  
EXPOSE 8181 8101 8778  
USER root  
  
ENV KARAF_VERSION 3.0.2  
ENV DEPLOY_DIR /deployments  
  
RUN yum install -y wget ruby  
  
# Install fonts  
# RUN \  
# echo "deb http://http.debian.net/debian jessie contrib" >>
/etc/apt/sources.list && \  
# apt-get update && \  
# echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections && \  
# apt-get install -y ttf-mscorefonts-installer  
RUN wget http://archive.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz -O /tmp/karaf.tar.gz  
  
# Unpack  
RUN tar xzf /tmp/karaf.tar.gz -C ${DEPLOY_DIR}  
RUN ln -s ${DEPLOY_DIR}/apache-karaf-${KARAF_VERSION} ${DEPLOY_DIR}/karaf  
RUN rm /tmp/karaf.tar.gz  
  
# Add configurtion templates  
# ADD users.properties ${DEPLOY_DIR}/apache-karaf-${KARAF_VERSION}/etc/  
ADD karaf ${DEPLOY_DIR}/apache-karaf-${KARAF_VERSION}/build  
  
# Remove unneeded apps  
RUN rm -rf ${DEPLOY_DIR}/karaf/deploy/README  
  
ENV KARAF_HOME ${DEPLOY_DIR}/karaf  
ENV PATH $PATH:$KARAF_HOME/bin  
  
# Copy deploy-and-run.sh for standalone images  
# Necessary to permit running with a randomised UID  
COPY deploy-run.sh ${DEPLOY_DIR}/deploy-run.sh  
RUN chmod a+x ${DEPLOY_DIR}/deploy-run.sh \  
&& chmod -R a+rwX ${DEPLOY_DIR}  
  
# S2I requires a numeric, non-0 UID  
USER 1000  
CMD ["usage"]  

