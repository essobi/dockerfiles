# Build using: docker build -f gocd-agent/Dockerfile -t gocd-agent .  
FROM java:openjdk-7-jre  
MAINTAINER Aravind SV <arvind.sv@gmail.com>  
  
RUN mkdir -p /var/run/go-agent  
  
WORKDIR /tmp  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
ENV GOCD_VERSION=15.2.0-2248  
ENV GOCD_AGENT_SHA1=2a970a5f7e83dd89813c48b261fa6ca11c2d4dcf  
ENV GOCD_AGENT_URL=https://download.go.cd/gocd-deb/go-agent-$GOCD_VERSION.deb  
RUN set -x \  
&& curl -fSL "$GOCD_AGENT_URL" -o go-agent.deb \  
&& echo "$GOCD_AGENT_SHA1 go-agent.deb" | sha1sum -c - \  
&& dpkg -i --debug=10 go-agent.deb \  
&& rm go-agent.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/lib/go-agent/config && rm -f /etc/default/go-agent  
  
ENV GO_SERVER=go-server  
ENV GO_SERVER_PORT=8153  
ENV AGENT_WORK_DIR=/var/lib/go-agent  
ENV AGENT_KEY=123456789abcdef  
ENV DAEMON=N  
ENV VNC=N  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
ADD go-agent-start.sh /usr/local/bin/go-agent  
  
CMD ["/bin/tini", "--", "/usr/local/bin/go-agent"]  

