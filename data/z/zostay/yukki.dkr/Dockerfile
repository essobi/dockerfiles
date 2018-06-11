FROM alpine:3.5  
LABEL maintainer="Sterling Hanenkamp \"sterling@hanenkamp.com\""  
  
RUN mkdir -p /usr/src/perl  
RUN mkdir -p /usr/src/yukki  
COPY perl/*.patch /usr/src/perl  
COPY yukki/*.patch /usr/src/yukki  
COPY special.yaml /  
  
ENV YUKKI_CONFIG="/var/yukki/wiki/etc/yukki.conf"  
ENV YUKKI_PORT=80  
RUN apk add --no-cache git libxml2 expat openssh \  
&& apk add --no-cache --virtual my-build-essentials curl g++ make wget
libxml2-dev expat-dev openssl openssl-dev  
  
WORKDIR /usr/src/perl  
RUN curl -SL https://www.cpan.org/src/5.0/perl-5.24.2.tar.bz2 -o
perl-5.24.2.tar.bz2 \  
&& echo 'e28c8fa588c4227eb25350036b45d7b1b46d61bb3a2194ee09dc79be6ed0fd0f
*perl-5.24.2.tar.bz2' | sha256sum -c - \  
&& tar --strip-components=1 -xjf perl-5.24.2.tar.bz2 -C /usr/src/perl \  
&& rm perl-5.24.2.tar.bz2 \  
&& cat *.patch | patch -p1 \  
&& ./Configure -Duse64bitall -Duseshrplib -des \  
&& make -j$(nproc) \  
&& make install  
  
# Tests always fail for me... skipping  
# && TEST_JOBS=$(nproc) make test_harness \  
WORKDIR /usr/src  
RUN curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
\  
&& chmod +x cpanm \  
&& ./cpanm App::cpanminus \  
&& rm -fr ./cpanm /root/.cpanm /usr/src/perl /tmp/  
  
RUN cpanm --notest Starman  
RUN cpanm --notest H/HA/HANENKAMP/Yukki-0.991_006.tar.gz  
  
# # Build from the master branch and debug  
# WORKDIR /usr/src/yukki  
# RUN git clone https://github.com/zostay/Yukki.git  
# WORKDIR /usr/src/yukki/Yukki  
# RUN cpanm --notest -v Dist::Zilla  
# RUN dzil authordeps --missing | cpanm --notest -v  
# RUN TZ=UTC dzil listdeps | cpanm --notest -v  
# RUN cpanm -v YAML  
# RUN TZ=UTC V=0.990_003 dzil install --install-command="cpanm --notest ."  
# WORKDIR /usr/src  
# #RUN rm -rf /usr/src/yukki  
RUN mkdir -p /var/yukki  
RUN apk del my-build-essentials  
COPY yukki-runner /usr/local/bin  
RUN chmod 755 /usr/local/bin/yukki-runner  
  
RUN yukki-setup /var/yukki/wiki \  
&& git config --global user.name Anonymous \  
&& git config --global user.email anonymous@localhost  
  
RUN cat /special.yaml >> /var/yukki/wiki/etc/yukki.conf \  
&& rm /special.yaml  
  
WORKDIR /var/yukki  
VOLUME /var/yukki  
EXPOSE 80  
ENTRYPOINT [ "/usr/local/bin/yukki-runner" ]  
CMD [ "yukki.psgi" ]  

