FROM ruby:2.4.2-jessie  
  
EXPOSE 9000  
ENV LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
GOVERSION="1.8" \  
GOPATH="/go" \  
GOROOT="/goroot"  
ENV IRC_NOTIFY_BRANCHES production  
  
ENV GHOSTBUSTER_VERSION 0.9.0  
RUN apt-get update \  
&& apt-get install -y locales-all \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install webhook  
RUN apt-get update \  
&& apt-get -y install git curl jq \  
&& apt-get install -y ca-certificates \  
&& curl https://storage.googleapis.com/golang/go${GOVERSION}.linux-
amd64.tar.gz | tar xzf - \  
&& mv /go ${GOROOT} \  
&& ${GOROOT}/bin/go get github.com/adnanh/webhook \  
&& rm -rf go${GOVERSION}.linux-amd64.tar.gz ${GOROOT} \  
&& apt-get clean  
  
RUN gem install puppet-ghostbuster --no-ri --no-rdoc --version
"${GHOSTBUSTER_VERSION}"  
  
COPY puppet-ghostbuster.json /etc/webhook/puppet-ghostbuster.json  
COPY puppet-ghostbuster.sh /puppet-ghostbuster.sh  
  
# Configure .ssh directory  
RUN mkdir /root/.ssh \  
&& chmod 0600 /root/.ssh \  
&& echo StrictHostKeyChecking no > /root/.ssh/config  
  
VOLUME ["/var/lib/git/"]  
  
COPY /docker-entrypoint.sh /  
COPY /gh-create-issues.sh /usr/local/bin/  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  

