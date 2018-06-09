# This software is Copyright (c) 2014 by Chris Weyl <chris.weyl@wps.io>  
#  
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0  
# International License (CC-BY-SA-4.0).  
#  
# http://creativecommons.org/licenses/by-sa/4.0/  
FROM rsrchboy/perlbrew-base:latest  
MAINTAINER Chris Weyl <chris.weyl@wps.io>  
  
ENV TARGET_PERL_FULL 5.24.0  
ENV TARGET_PERL stable  
  
RUN perlbrew download $TARGET_PERL_FULL  
RUN perlbrew install -j4 --as $TARGET_PERL $TARGET_PERL_FULL && rm -rf
/usr/local/perlbrew/build/*  
  
RUN perlbrew switch $TARGET_PERL  
  
ENV PATH /usr/local/perlbrew/perls/$TARGET_PERL/bin:$PATH  
ENV MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_MANPATH /usr/local/perlbrew/perls/$TARGET_PERL/man  
ENV PERLBREW_PATH
/usr/local/perlbrew/bin:/usr/local/perlbrew/perls/$TARGET_PERL/bin  
ENV PERLBREW_PERL $TARGET_PERL  
  
RUN perlbrew info  
RUN perl -v  

