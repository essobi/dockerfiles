FROM debian:jessie  
  
MAINTAINER Dariusz Gafka <d.gafka@madkom.pl>  
  
ENV PACT_MOCK_SERVICE "2.1.0"  
ENV RAKE "10.4.2"  
ADD ./provider /opt/provider  
  
RUN apt-get update -y && \  
apt-get install -y wget ruby-dev rubygems --no-install-recommends && \  
mkdir /opt/gems && \  
gem install hoe minitest && gem install rake -v $RAKE && \  
gem install pact-provider-proxy -v $PACT_MOCK_SERVICE && \  
mkdir contract && ln -s /contract /opt/provider/spec/pacts && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/contract"]  
VOLUME ["/opt/provider/log"]  
VOLUME ["/opt/provider/reports"]  
  
WORKDIR /opt/provider  
  
CMD "/usr/local/bin/rake"

