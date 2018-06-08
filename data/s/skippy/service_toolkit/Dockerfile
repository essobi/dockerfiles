FROM debian:wheezy  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
ENV CONFD_VERSION 0.6.3  
RUN echo "deb http://cdn.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list  
  
# Install Haproxy.  
# sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \  
RUN apt-get update -y && \  
apt-get install -y -q --no-install-recommends \  
haproxy -t wheezy-backports && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install confd. TODO: use a released confd when 0.7 is released  
# ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /usr/local/bin/confd  
# RUN echo 'e3edd9667b98ea32ae504bb7987bb0a269479267 /usr/local/bin/confd' >
/tmp/confd.sha1 && \  
# sha1sum --check /tmp/confd.sha1 && \  
# rm /tmp/* && \  
# chmod +x /usr/local/bin/confd  
ADD confd-custom-linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
ADD haproxy_configuration.toml /etc/confd/conf.d/haproxy_configuration.toml  
ADD haproxy.tmpl /etc/confd/templates/haproxy.tmpl  
#RUN chown -R daemon:daemon /etc/haproxy /var/lib/haproxy  
# install Python  
RUN apt-get update -y && \  
apt-get install -y -q --no-install-recommends \  
python2.7-minimal \  
python-pip \  
openssl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN /usr/bin/pip -q install requests boto3  
  
ADD service-toolkit /usr/local/bin/service-toolkit  
RUN chmod +x /usr/local/bin/service-toolkit  
  
#USER daemon  
ENTRYPOINT ["/usr/local/bin/service-toolkit"]  
CMD ["--help"]  

