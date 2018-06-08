FROM rocker/tidyverse  
ENV RAKUDO=2018.04  
ARG BUILD_DATE  
  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
maintainer="Dr Suman Khanal <suman81765@gmail.com>"  
  
#WORKDIR /  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git nano libzmq3-dev libssl-dev curl wget imagemagick python3-pip \  
&& pip3 install wheel setuptools --no-cache-dir \  
&& pip3 install asciinema --no-cache-dir \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget http://rakudo.org/downloads/star/rakudo-star-${RAKUDO}.tar.gz \  
&& tar -xvzf rakudo-star-${RAKUDO}.tar.gz \  
&& cd rakudo-star-${RAKUDO} \  
&& perl Configure.pl --prefix=/usr --gen-moar --backends=moar \  
&& make && make install \  
&& cd .. && rm -rf rakudo-star-${RAKUDO}.tar.gz rakudo-star-${RAKUDO} \  
&& export PATH=/usr/bin:/usr/share/perl6/site/bin:$PATH \  
&& zef install App::Mi6 \  
&& apt-get auto-remove  
  
ENV RUSTUP_HOME=/usr/local/rustup \  
CARGO_HOME=/usr/local/cargo  
  
RUN set -eux; \  
\  
url="https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-
init"; \  
wget "$url"; \  
chmod +x rustup-init; \  
./rustup-init -y --no-modify-path --default-toolchain stable; \  
rm rustup-init; \  
chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \  
rm /etc/profile  
  
ADD profile /etc/profile  

