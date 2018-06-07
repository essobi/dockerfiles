# stage 1 - building livegrep  
FROM ubuntu:16.04 as builder  
RUN apt-get update && apt-get -y install \  
gcc-4.8 \  
g++-4.8 \  
libxml2-utils \  
wget \  
pkg-config \  
zip \  
unzip \  
zlib1g-dev \  
openjdk-8-jdk \  
git \  
openssh-client \  
python  
  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-173.0.0-linux-x86_64.tar.gz /tmp/gcloud.tar.gz  
RUN tar -C /usr/local/ -xzf /tmp/gcloud.tar.gz  
RUN /usr/local/google-cloud-sdk/install.sh  
  
RUN wget --quiet -O /tmp/bazel-0.8.1-installer-linux-x86_64.sh \  
'https://github.com/bazelbuild/bazel/releases/download/0.8.1/bazel-0.8.1-installer-
linux-x86_64.sh' && \  
chmod +x /tmp/bazel-0.8.1-installer-linux-x86_64.sh  
RUN /tmp/bazel-0.8.1-installer-linux-x86_64.sh  
  
# build livegrep  
COPY ./ /livegrep/  
RUN cd /livegrep && bazel build --spawn_strategy=standalone
--genrule_strategy=standalone //...  
RUN mv /livegrep/bazel-bin /livegrep/bazel-bin-bak && \  
cp -r --dereference $(readlink -f /livegrep/bazel-bin-bak) /livegrep/bazel-bin  
  
# stage 2 - setting up production image  
FROM ubuntu:16.04  
COPY \--from=builder /livegrep/ /livegrep/  
WORKDIR /livegrep  
  
EXPOSE 9999  
RUN apt-get update && apt-get -y install curl && rm -rf /var/lib/apt/lists/*  
HEALTHCHECK CMD curl -f http://localhost:9999/ || exit 1  
  
ENTRYPOINT ["bazel-bin/src/tools/codesearch", "-listen",
"tcp://localhost:9999", "doc/examples/livegrep/index.json"]  

