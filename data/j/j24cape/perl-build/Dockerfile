FROM buildpack-deps:jessie  
MAINTAINER NISHIZAKI Tadashi <j24cape@gmail.com>  
  
RUN curl -s https://raw.githubusercontent.com/tokuhirom/Perl-
Build/master/perl-build > /usr/bin/perl-build \  
&& perl -pi -e 's%^#!/usr/bin/env perl%#!/usr/bin/perl%g' /usr/bin/perl-build
\  
&& chmod +x /usr/bin/perl-build  
  
CMD ["perl-build", "--version"]  

