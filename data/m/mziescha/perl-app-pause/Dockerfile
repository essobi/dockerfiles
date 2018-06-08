FROM mziescha/cpan-module-test  
  
MAINTAINER Mario Zieschang <mziescha@cpan.org>  
  
RUN apk add --update g++ gcc openssl openssl-dev \  
&& cpanm \  
LWP::UserAgent \  
LWP::Protocol::https::Socket \  
Exporter::Tiny \  
App::pause \  
&& apk del g++ gcc \  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/* /root/.cpanm/* /usr/share/man/*
/usr/local/share/man/*  
  
WORKDIR /app

