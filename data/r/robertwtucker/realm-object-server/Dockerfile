FROM buildpack-deps:xenial-curl  
  
# Install & setup Realm's PackageCloud repository  
RUN set -x \  
&& curl -L https://packagecloud.io/realm/realm/gpgkey | apt-key add - \  
&& apt-get update -qq \  
&& apt-get install -y apt-transport-https --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& \  
{ \  
echo "deb https://packagecloud.io/realm/realm/ubuntu/ xenial main"; \  
echo "deb-src https://packagecloud.io/realm/realm/ubuntu/ xenial main"; \  
} > /etc/apt/sources.list.d/realm_realm.list  
  
ENV REALM_VERSION 1.7.4-5  
# Update the repository and install Realm  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get -y install realm-object-server-developer=${REALM_VERSION} \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /var/lib/realm/object-server  
EXPOSE 9080  
  
CMD ["/usr/bin/realm-object-server", "-c", "/etc/realm/configuration.yml"]  

