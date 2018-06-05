###############################################################################  
# Rakudo Pulsar  
#  
# A bleeding edge Rakudo Perl 6 distribution in a Docker container.  
#  
# Comes with 'zef' for module management.  
#  
###############################################################################  
  
FROM debian:sid  
MAINTAINER Tim Totten  
  
ENV BUILD_DEPS=' \  
git \  
gcc \  
libc6-dev \  
libencode-perl \  
make \  
'  
  
RUN RUN_DEPS=' \  
perl \  
ca-certificates \  
procps \  
curl \  
rlwrap \  
' \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $RUN_DEPS $BUILD_DEPS \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone git://github.com/rakudo/rakudo.git /usr/src/rakudo \  
&& ( \  
cd /usr/src/rakudo \  
&& perl Configure.pl --prefix=/usr --gen-moar \  
&& make install \  
) \  
&& git clone git://github.com/ugexe/zef.git /usr/src/zef \  
&& ( \  
cd /usr/src/zef \  
&& perl6 -Ilib bin/zef install . \  
) \  
&& rm -rf /usr/src/rakudo \  
&& rm -rf /usr/src/zef  
  
ENV PATH=$PATH:/usr/share/perl6/site/bin  
  

