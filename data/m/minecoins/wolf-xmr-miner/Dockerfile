FROM ubuntu:16.04  
  
WORKDIR /opt/wolf-xmr-miner  
  
RUN apt-get update \  
&& apt-get -qq --no-install-recommends install \  
libjansson-dev \  
ocl-icd-opencl-dev \  
&& rm -r /var/lib/apt/lists/*  
  
RUN set -x \  
&& buildDeps=' \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
make \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p src \  
&& cd src \  
&& curl -sL https://github.com/wolf9466/wolf-xmr-miner/tarball/master | tar
-xz --strip-components=1 \  
&& make -j"$(nproc)" \  
&& install -pm755 miner ../ \  
&& install -pm644 xmr.conf ../ \  
&& sed -ri \  
-e 's/("user": ).*/\1"49TfoHGd6apXxNQTSHrMBq891vH6JiHmZHbz5Vx36nLRbz6WgcJunTtgcxnoG6snKFeGhAJB5LjyAEnvhBgCs5MtEgML3LU",/' \  
../xmr.conf \  
\  
&& install -pm644 README.md ../ \  
&& cd .. \  
&& rm -r src \  
&& apt-get -qq --auto-remove purge $buildDeps  
  
ENTRYPOINT ["./miner"]  
CMD ["xmr.conf"]  

