FROM debian:jessie  
  
RUN apt-get update \  
&& GIT_DEPS=' \  
ca-certificates \  
git \  
' \  
OTHER_DEPS=' \  
build-essential \  
cmake \  
' \  
BUILD_DEPS="${GIT_DEPS} ${OTHER_DEPS}" \  
# 5.5.31  
&& TIDY5_COMMIT_ID=e48b06b8c078c9d10f0711bbcf579c748c8b475c \  
&& apt-get install -y --no-install-recommends ${BUILD_DEPS} \  
&& git clone https://github.com/htacg/tidy-html5.git /tmp/tidy-html5 \  
&& cd /tmp/tidy-html5 \  
&& git checkout ${TIDY5_COMMIT_ID} \  
&& cd /tmp/tidy-html5 \  
&& cd build/cmake \  
&& cmake ../.. -DCMAKE_INSTALL_PREFIX=/usr/local \  
&& make \  
&& make install \  
&& rm -rf /tmp/tidy-html5 \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["tidy"]  
CMD ["--help"]  

