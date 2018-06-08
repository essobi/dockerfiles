FROM puppet/puppetserver  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="puppetserver" \  
org.label-schema.description="puppetserver with puppet-agent hiera-eyaml
msgpack." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/puppetserver" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --name=puppetserver -p 8140:8140 -h
larp -d jorgeandrada/puppetserver"  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -fy puppet-agent \  
&& gem install hiera-eyaml \  
&& puppetserver gem install hiera-eyaml \  
&& puppetserver gem install msgpack \  
&& gem cleanup all \  
&& rm -rf /var/lib/apt/lists/*  

