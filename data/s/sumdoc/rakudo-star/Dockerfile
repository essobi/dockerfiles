FROM debian:sid  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
PANDOC=2.2.1-1 \  
RAKUDO=2018.04  
  
LABEL maintainer="Dr Suman Khanal <suman81765@gmail.com>"  
#ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get install -y build-essential git \  
nano libzmq3-dev ca-certificates libssl-dev curl wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget http://rakudo.org/downloads/star/rakudo-star-${RAKUDO}.tar.gz \  
&& tar -xvzf rakudo-star-${RAKUDO}.tar.gz \  
&& rm -rf rakudo-star-${RAKUDO}.tar.gz \  
&& cd rakudo-star-${RAKUDO} \  
&& perl Configure.pl --prefix=/usr --gen-moar --backends=moar \  
&& make && make install \  
&& cd .. && rm -rf rakudo-star-${RAKUDO} \  
&& export PATH=/usr/bin:/usr/share/perl6/site/bin:$PATH \  
&& zef install App::Mi6 \  
&& wget
https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-${PANDOC}-amd64.deb
\  
&& dpkg -i pandoc-${PANDOC}-amd64.deb && rm pandoc-${PANDOC}-amd64.deb \  
&& apt-get purge -y --auto-remove build-essential  
  
#--no-install-recommends  
  
ENV PATH $PATH:/usr/bin:/usr/share/perl6/site/bin  
CMD ["perl6", "--version"]  

