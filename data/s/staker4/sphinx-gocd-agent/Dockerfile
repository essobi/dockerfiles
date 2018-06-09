FROM staker4/sphinx-autobuild  
  
MAINTAINER Raymond Tiefengraber  
  
# Install apt packages  
RUN apt-get update \  
&& apt-get -y install \  
openjdk-8-jre-headless \  
git \  
subversion \  
  
# Clean downloaded apt packages after install  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /  
  
# Ensure that the container logs on stdout  
ADD log4j.properties /var/lib/go-agent/log4j.properties  
ADD log4j.properties /var/lib/go-agent/go-agent-log4j.properties  
# Add go user  
RUN adduser -home /go --system --disabled-password go  
  
ADD https://github.com/ketan/gocd-golang-
bootstrapper/releases/download/0.9/go-bootstrapper-0.9.linux.amd64 /go/go-
agent  
RUN chmod 755 /go/go-agent  
  
ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini /tini  
RUN chmod +x /tini  
  
# Set runtime entrypoint to execute go-agent  
ENTRYPOINT ["/tini", "--"]  
USER go  
CMD /go/go-agent

