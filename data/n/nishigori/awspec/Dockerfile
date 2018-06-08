FROM ruby:2.4-alpine  
  
# https://github.com/k1LoW/awspec/releases  
ENV AWSPEC_VER 1.2.0  
RUN set -x \  
&& apk upgrade --no-cache \  
&& gem install --no-document awspec -v $AWSPEC_VER \  
&& mkdir -p /awspec  
  
WORKDIR /awspec  
ENTRYPOINT ["rspec"]  
CMD []  

