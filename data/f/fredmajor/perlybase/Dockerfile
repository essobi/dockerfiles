# Based on a container from rschboy repository on main docker hub, with my
adjustments  
FROM rsrchboy/perlbrew-base:latest  
MAINTAINER Fred Major major.freddy@yahoo.com  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
ENV TARGET_PERL_FULL stable  
ENV TARGET_PERL stable_threads  
  
RUN perlbrew install --thread --as $TARGET_PERL $TARGET_PERL_FULL && rm -rf
/usr/local/perlbrew/build/*  
  
RUN perlbrew switch $TARGET_PERL  
  
ENV PATH /usr/local/perlbrew/perls/$TARGET_PERL/bin:$PATH  
ENV MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_PATH
/usr/local/perlbrew/bin:/usr/local/perlbrew/perls/$TARGET_PERL/bin  
ENV PERLBREW_PERL $TARGET_PERL  
  
RUN apt-get update && apt-get -y install pkg-config libcurl4-gnutls-dev tidy
libxml2 libxml2-dev  
RUN cpanm Carton ExtUtils::PkgConfig  
  
RUN perlbrew info  
RUN perl -v  

