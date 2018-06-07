FROM gushry/deps  
  
### Java  
ENV JAVA_VERSION 8u45  
ENV JAVA_DEBIAN_VERSION 8u45-b14-2~bpo8+2  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION"  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
### New Relic  
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list \  
&& wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& apt-get update \  
&& apt-get install newrelic-sysmond  
ADD dummy.nrsysmond.cfg /etc/newrelic/nrsysmond.cfg  
RUN chmod +r /etc/newrelic/nrsysmond.cfg  
ADD scripts /opt/scripts  
RUN ls -lR /opt  
RUN ls -lR /etc/newrelic  
RUN chmod +x /opt/scripts/newrelic.sh  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/opt/scripts/newrelic.sh"]  
  

