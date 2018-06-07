FROM ubuntu:14.04  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Prepare the Build Environment  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
# from the build instructions  
openjdk-7-jdk \  
bison \  
g++-multilib \  
git-core \  
gperf \  
libxml2-utils \  
make \  
python-networkx \  
zlib1g-dev:i386 \  
zip \  
# Additional dependencies  
unzip \  
curl \  
openssh-client \  
ca-certificates \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add unprivileged user  
ARG FAIRPHONE_UID  
RUN useradd -s /bin/bash -u ${FAIRPHONE_UID:-1000} -U -m fairphone  
  
# Install repo  
ARG REPO_VERSION=1.23  
ARG
REPO_SHA256=e147f0392686c40cfd7d5e6f332c6ee74c4eab4d24e2694b3b0a0c037bf51dc5  
RUN curl https://storage.googleapis.com/git-repo-
downloads/repo-${REPO_VERSION} -o /usr/local/bin/repo && \  
echo "${REPO_SHA256} /usr/local/bin/repo" | sha256sum -c && \  
chmod +x /usr/local/bin/repo  
  
# Setup working directory  
ENV FP_DATA_VOLUME /var/fairphone_os/  
ENV FP_WORKDIR ${FP_DATA_VOLUME}/build  
ENV FP_LOGDIR ${FP_DATA_VOLUME}/logs  
ENV PATH /opt/helper_scripts:$PATH  
  
RUN mkdir -p ${FP_DATA_VOLUME} && chown -R fairphone:fairphone
${FP_DATA_VOLUME}  
VOLUME ${FP_DATA_VOLUME}  
WORKDIR ${FP_DATA_VOLUME}  
  
USER fairphone  

