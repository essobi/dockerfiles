FROM ruby:2.3-alpine  
  
MAINTAINER https://github.com/realestate-com-au/stackup  
  
ENV SHUSH_VERSION 1.3.2  
ENV STACKUP_VERSION 1.1.1  
RUN apk update && apk add --no-cache curl diffutils \  
&& curl -sL -o /usr/local/bin/shush https://github.com/realestate-com-
au/shush/releases/download/v${SHUSH_VERSION}/shush_linux_amd64 \  
&& chmod +x /usr/local/bin/shush  
  
WORKDIR /app  
  
RUN curl -sL -o /tmp/stackup.zip https://github.com/realestate-com-
au/stackup/archive/v${STACKUP_VERSION}.zip && \  
cd /tmp && unzip -q stackup.zip && \  
mv /tmp/stackup-${STACKUP_VERSION}/bin /app/. && \  
mv /tmp/stackup-${STACKUP_VERSION}/lib /app/. && \  
mv /tmp/stackup-${STACKUP_VERSION}/spec /app/. && \  
mv /tmp/stackup-${STACKUP_VERSION}/README.md /app/. && \  
mv /tmp/stackup-${STACKUP_VERSION}/CHANGES.md /app/. && \  
mv /tmp/stackup-${STACKUP_VERSION}/stackup.gemspec /app/.  
  
RUN gem build stackup.gemspec  
RUN gem install stackup-*.gem  
  
ENTRYPOINT ["/usr/local/bin/shush","exec","--","stackup"]  

