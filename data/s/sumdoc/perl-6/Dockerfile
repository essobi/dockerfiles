FROM debian:sid  
  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
PANDOC=2.1.3-1  
ARG BUILD_DATE="2018-03-06"  
LABEL org.label-schema.vcs-url="https://github.com/sumandoc/Perl-6" \  
org.label-schema.build-date=$BUILD_DATE \  
maintainer="Dr Suman Khanal <suman81765@gmail.com>"  
  
WORKDIR /  
  
RUN apt-get update \  
&& apt-get install -y build-essential \  
git nano libzmq3-dev ca-certificates curl wget asciinema \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/rakudo/rakudo.git \  
&& cd rakudo && perl Configure.pl --prefix=/usr --gen-moar --gen-nqp
--backends=moar \  
&& make && make install && cd .. && rm -rf rakudo \  
&& git clone https://github.com/ugexe/zef.git && cd zef && perl6 -Ilib bin/zef
install . \  
&& cd .. && rm -rf zef \  
&& export PATH=$PATH:/usr/share/perl6/site/bin \  
&& zef install Linenoise App::Mi6 --force-test \  
&& wget
https://github.com/jgm/pandoc/releases/download/2.1.3/pandoc-${PANDOC}-amd64.deb
\  
&& dpkg -i pandoc-${PANDOC}-amd64.deb && rm pandoc-${PANDOC}-amd64.deb \  
&& apt-get purge -y --auto-remove build-essential  
  
#--no-install-recommends  
ENV PATH /usr/share/perl6/site/bin:$PATH  
CMD ["perl6", "--version"]  

