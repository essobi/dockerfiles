FROM openjdk:8  
ENV APACHEDS_VERSION 2.0.0-M24  
ENV APACHEDS_DEB_MIRROR
https://archive.apache.org/dist/directory/apacheds/dist/${APACHEDS_VERSION}/apacheds-${APACHEDS_VERSION}-amd64.deb  
  
ENV MD5SUM 18c319bd11884db3bce079e9e2bfe491 /tmp/apacheds.deb  
  
COPY docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh  
COPY apacheds-2.0.0-M24-amd64.deb.asc /tmp/apacheds.deb.asc  
  
# Download the chosen Apache DS version  
RUN wget -O /tmp/apacheds.deb ${APACHEDS_DEB_MIRROR} && \  
# Download the KEYS  
wget -O /tmp/KEYS https://www.apache.org/dist/directory/KEYS && \  
# And verify the signature and the MD5SUM  
gpg --import /tmp/KEYS && \  
gpg --verify /tmp/apacheds.deb.asc && \  
echo ${MD5SUM} | md5sum -c - && \  
# Now install the downloaded .deb along with any dependency it may carry  
apt-get update -y && \  
apt-get install -y \  
/tmp/apacheds.deb && \  
rm -rf /tmp && \  
# This is needed for our docker_entrypoint.sh  
chmod g=u /etc/passwd && \  
# Our OpenShift user will belong to group 0  
chgrp -R 0 /var/lib/apacheds-${APACHEDS_VERSION} && \  
chmod -R g+rwX /var/lib/apacheds-${APACHEDS_VERSION}  
  
USER 1000  
EXPOSE 10389 10636  
VOLUME [ "/var/lib/apacheds-2.0.0-M24" ]  
  
ENTRYPOINT [ "/usr/local/bin/docker_entrypoint.sh" ]  
CMD [ "/opt/apacheds-2.0.0-M24/bin/apacheds", "console", "default" ]

