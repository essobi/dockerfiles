FROM debian:jessie  
  
EXPOSE 9000  
ENV \  
GOVERSION="1.8" \  
GOPATH="/go" \  
GOROOT="/goroot" \  
R10K_VERSION='2.4.5+RK-291-forge_module_caching'  
# Install webhook  
RUN apt-get update \  
&& apt-get -y install git curl rubygems \  
&& apt-get install -y ca-certificates \  
&& curl https://storage.googleapis.com/golang/go${GOVERSION}.linux-
amd64.tar.gz | tar xzf - \  
&& mv /go ${GOROOT} \  
&& ${GOROOT}/bin/go get github.com/adnanh/webhook \  
&& rm -rf go${GOVERSION}.linux-amd64.tar.gz ${GOROOT} \  
&& apt-get clean  
  
# Install r10k  
RUN gem install specific_install --no-ri --no-rdoc \  
&& gem specific_install -l https://github.com/camptocamp/r10k.git -b
$R10K_VERSION  
  
# Configure .ssh directory  
RUN mkdir /root/.ssh \  
&& chmod 0600 /root/.ssh \  
&& echo StrictHostKeyChecking no > /root/.ssh/config  
  
# Configure volumes  
VOLUME ["/opt/puppetlabs/r10k/cache/", "/etc/puppetlabs/code/environments"]  
  
RUN useradd -r -s /bin/false r10k  
COPY r10k.json /etc/webhook/r10k.json  
RUN chown -R r10k. /etc/webhook  
  
COPY push-to-r10k.sh /push-to-r10k.sh  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

