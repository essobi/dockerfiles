FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
collectd \  
librrd-ruby \  
ruby \  
ruby-dev \  
rubygems \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV VISAGE_VERSION 2.1.0  
RUN echo "gem: --bindir /usr/bin --no-ri --no-rdoc" > ~/.gemrc  
RUN gem install visage-app -v $VISAGE_VERSION  
RUN sed -i 's|\\(Rack::Server.new(:config => config, :Port => port, :server =>
"webrick"\\)|\1, :Host => "0.0.0.0"|g' /var/lib/gems/2.1.0/gems/visage-
app-${VISAGE_VERSION}/bin/visage-app  
  
EXPOSE 9292  
CMD visage-app start  

