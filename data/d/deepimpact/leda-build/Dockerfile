FROM buildpack-deps:stretch-scm  
  
ENV LEIN_ROOT=1 \  
LANG=C.UTF-8 \  
DOCKER_BUCKET="get.docker.com" \  
DOCKER_VERSION="1.12.1" \  
DOCKER_SHA256="05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79"
\  
DIND_COMMIT="3b5fac462d21ca164b3778647420016315289034"  
  
COPY dockerd-entrypoint.sh /usr/local/bin/  
  
RUN apt-get update \  
&& apt-get install -y python3-pip libyaml-dev python3.5-dev zip libzmq-jni
openjdk-8-jdk-headless \  
&& apt-get install -y --no-install-recommends e2fsprogs iptables xfsprogs xz-
utils \  
&& pip3 install awscli pyminifier cython \  
&& curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein && chmod a+x /usr/local/bin/lein && lein \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box  
&& addgroup dockremap \  
&& useradd -g dockremap dockremap \  
&& echo 'dockremap:165536:65536' >> /etc/subuid \  
&& echo 'dockremap:165536:65536' >> /etc/subgid \  
&& wget
"https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -O
/usr/local/bin/dind \  
&& chmod +x /usr/local/bin/dind \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -fr /tmp/* \  
&& apt-get clean  
  
VOLUME /var/lib/docker  
  
ENTRYPOINT ["dockerd-entrypoint.sh"]

