# Divolte  
#  
# Divolte Documentation:  
# www.divolte.io  
#  
FROM openjdk:8-jre-slim  
  
#  
# Configuration  
#  
ARG BUILD_DATE  
ARG DIVOLTE_VERSION=0.7.0  
ARG ENABLE_KERBEROS=no  
ENV ENABLE_KERBEROS=$ENABLE_KERBEROS  
  
  
LABEL org.label-schema.name="Divolte ${DIVOLTE_VERSION}" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$DIVOLTE_VERSION  
  
#  
# Install dependencies and Divolte  
#  
RUN apt-get update && \  
if [ "$ENABLE_KERBEROS" = "yes" ]; then\  
apt-get install -y curl krb5-user;\  
else\  
apt-get install -y curl;\  
fi && \  
mkdir -p /opt/divolte && \  
cd /tmp/ && \  
curl -O http://divolte-releases.s3-website-eu-west-1.amazonaws.com/divolte-
collector/${DIVOLTE_VERSION}/distributions/divolte-
collector-${DIVOLTE_VERSION}.tar.gz && \  
echo "9a6c81a2290284952389050d039e0b3c9ac31f2af989eec1067b58da12557151
divolte-collector-${DIVOLTE_VERSION}.tar.gz" | sha256sum -c - && \  
tar zxpf divolte-collector-${DIVOLTE_VERSION}.tar.gz -C /opt/divolte && \  
mv /opt/divolte/divolte-collector-${DIVOLTE_VERSION}/ /opt/divolte/divolte-
collector && \  
apt-get remove -y curl && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -fr /var/tmp/* /tmp/*  
  
#  
# Configuration changes using divolte-collector.conf  
#  
COPY conf/ /opt/divolte/divolte-collector/conf/  
  
COPY configureKerberosClient.sh /opt/divolte/  
COPY start.sh /opt/divolte/  
  
#  
# Expose the Divolte Collector click simulation web page  
#  
EXPOSE 8290  
CMD ["/opt/divolte/start.sh"]  

