# Tiny little proselint image that will pull the POD out of a Perl file  
# (passed on STDIN) and lint it  
#  
# Chris Weyl <cweyl@alumni.drew.edu> 2017  
FROM alpine:3.6  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
RUN apk update && \  
apk add \  
wget make gcc perl-dev musl-dev \  
perl perl-moose perl-namespace-autoclean perl-sub-exporter \  
perl-extutils-config perl-extutils-installpaths \  
perl-encode \  
py2-pip && \  
rm -r /var/cache/  
  
RUN pip install --no-cache-dir proselint  
  
COPY cpanm /bin/cpanm  
RUN cpanm -q Devel::OverloadInfo List::Util Pod::Elemental || ( cat
"$HOME/.cpanm/build.log" ; exit 1 ) \  
&& rm -rf "$HOME/.cpanm/"  
  
COPY do-proselint.sh /bin/do-proselint.sh  
COPY perl-to-pod-text.pl /bin/perl-to-pod-text.pl  
  
ENTRYPOINT [ "do-proselint.sh" ]  

