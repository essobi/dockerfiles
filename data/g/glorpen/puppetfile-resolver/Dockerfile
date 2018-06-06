FROM alpine:3.7  
LABEL maintainer="Arkadiusz Dzięgiel <arkadiusz.dziegiel@glorpen.pl>"  
  
ARG R10K_VERSION="2.5.5"  
RUN apk update \  
&& apk add ruby git shadow \  
&& rm -rf /var/cache/apk/*  
  
ADD r10k-forge-cache.patch /usr/local/share/  
  
# add r10k to puppet ruby instalation  
RUN gem install r10k:${R10K_VERSION} json_pure --no-ri --no-rdoc \  
&& cd /usr/lib/ruby/gems/*/gems/r10k-${R10K_VERSION}/ && patch -p1 <
/usr/local/share/r10k-forge-cache.patch \  
&& rm -rf /usr/lib/ruby/gems/*/cache  
  
ADD r10k.yaml /etc/puppetlabs/r10k/r10k.yaml  
ADD resolve.sh /usr/local/bin/puppetfile-resolve  
  
CMD ["/usr/local/bin/puppetfile-resolve"]  
  
# Metadata.  
LABEL \  
org.label-schema.name="pupetfile-resolver" \  
org.label-schema.description="This container will simply checkout modules in
given Puppetfile" \  
org.label-schema.version="1.0" \  
org.label-schema.vcs-url="https://github.com/glorpen/docker-puppetfile-
resolver" \  
org.label-schema.schema-version="1.0"  

