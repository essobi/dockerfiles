FROM j24cape/perl-build:jessie  
MAINTAINER NISHIZAKI Tadashi <j24cape@gmail.com>  
  
ENV BUILD_PERL_VER 5.22  
ENV BUILD_PERL_REL 2  
  
RUN perl-build -DDEBUGGING=-g $BUILD_PERL_VER.$BUILD_PERL_REL
/opt/perl-$BUILD_PERL_VER > /tmp/perl-build.log 2>&1 \  
&& echo "export PATH=/opt/perl-$BUILD_PERL_VER/bin:\$PATH" >
/etc/profile.d/perl-build.sh \  
&& curl -s https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm \  
| /opt/perl-$BUILD_PERL_VER/bin/perl \- -q --notest \  
App::cpanminus \  
App::cpanoutdated \  
> /tmp/cpanm.log 2>&1 \  
&& rm -fr /root/.cpanm /tmp/*  
  
ENV PATH /opt/perl-$BUILD_PERL_VER/bin:$PATH  
  
CMD ["perl", "-v"]  

