FROM debian:8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -yq && \  
apt-get install -yq --no-install-recommends build-essential curl ca-
certificates tar bzip2 patch && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ENV PERL_VERSION 5.8.8  
ENV PATH /opt/perl-$PERL_VERSION/bin:$PATH  
  
RUN curl https://raw.githubusercontent.com/tokuhirom/Perl-Build/master/perl-
build | perl \- $PERL_VERSION /opt/perl-$PERL_VERSION/  
RUN curl -sL https://cpanmin.us | perl \- --notest App::cpanminus Carton  

