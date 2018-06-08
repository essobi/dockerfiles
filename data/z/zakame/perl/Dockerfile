FROM buildpack-deps:wheezy  
MAINTAINER Zak B. Elep <zakame@cpan.org>  
  
RUN apt-get update \  
&& apt-get install -y curl procps \  
&& rm -fr /var/lib/apt/lists/*  
  
RUN mkdir /usr/src/perl  
COPY *.patch /usr/src/perl/  
WORKDIR /usr/src/perl  
  
RUN curl -SL
https://cpan.metacpan.org/authors/id/F/FL/FLORA/perl-5.14.2.tar.bz2 -o
perl-5.14.2.tar.bz2 \  
&& echo 'e48d11c6fd1ee61985b475d7f261d774296a1367 *perl-5.14.2.tar.bz2' |
sha1sum -c - \  
&& tar --strip-components=1 -xjf perl-5.14.2.tar.bz2 -C /usr/src/perl \  
&& rm perl-5.14.2.tar.bz2 \  
&& cat *.patch | patch -p1 \  
&& ./Configure -Duse64bitall -Duseshrplib -A ccflags=-fwrapv -des \  
&& make -j$(nproc) \  
&& TEST_JOBS=$(nproc) make test_harness \  
&& make install \  
&& cd /usr/src \  
&& curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
\  
&& chmod +x cpanm \  
&& ./cpanm App::cpanminus \  
&& rm -fr ./cpanm /root/.cpanm /usr/src/perl /tmp/*  
  
WORKDIR /root  
  
CMD ["perl5.14.2","-de0"]  

