FROM alpine  
  
MAINTAINER Mario Zieschang <mziescha@cpan.org>  
  
RUN apk add --update perl make curl g++ gcc wget perl-dev openssl openssl-dev
\  
&& curl -L https://cpanmin.us | perl - App::cpanminus \  
&& cpanm \  
Carp \  
Pod::Usage \  
Getopt::Long \  
DDP \  
Term::ReadKey \  
Pod::Coverage::TrustPod \  
Pod::Usage \  
Test::CheckManifest \  
Test::Pod \  
Test::Pod::Coverage \  
Test::Requires \  
Test::Spelling \  
Test::Net::LDAP \  
Devel::Cover \  
Devel::Cover::Report::Coveralls \  
Test::Simple \  
Test::Without::Module \  
Test::Warnings \  
Test::Needs \  
Test2::Suite \  
Test2::Plugin::NoWarnings \  
Test::RequiresInternet \  
&& apk del g++ gcc openssl-dev \  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/* /root/.cpanm/* /usr/share/man/*
/usr/local/share/man/*  

