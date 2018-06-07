# Base image  
FROM yongjhih/android:jdk8-all  
  
MAINTAINER Infer  
  
# Debian config  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
autoconf \  
curl \  
gcc \  
git \  
groff \  
libc6-dev \  
libgmp-dev \  
libmpc-dev \  
libmpfr-dev \  
m4 \  
make \  
ncurses-dev \  
ocaml \  
pkg-config \  
python-software-properties \  
rsync \  
software-properties-common \  
unzip \  
zlib1g-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV OPAM_VERSION 1.2.2  
# Install OPAM  
RUN curl -sL \  
https://github.com/ocaml/opam/releases/download/$OPAM_VERSION/opam-${OPAM_VERSION}-x86_64-Linux
\  
-o /usr/local/bin/opam && \  
chmod 755 /usr/local/bin/opam && \  
((/usr/local/bin/opam --version | grep -q $OPAM_VERSION) || \  
(echo "failed to download opam from GitHub."; exit 1))  
RUN opam init -y --comp=4.02.3  
  
ENV INFER_VERSION v0.8.1  
# Download the latest Infer release  
RUN cd /opt && \  
curl -sL \  
https://github.com/facebook/infer/releases/download/${INFER_VERSION}/infer-
linux64-${INFER_VERSION}.tar.xz | \  
tar xJ && \  
rm -f /infer && \  
ln -s ${PWD}/infer-linux64-$INFER_VERSION /infer  
  
WORKDIR /infer  
  
# Install opam dependencies  
RUN eval $(opam config env) && \  
opam update && \  
opam pin add --yes --no-action infer . && \  
opam install --deps-only infer  
  
# Compile Infer  
RUN eval $(opam config env) && \  
./build-infer.sh  
  
# Install Infer  
ENV INFER_HOME /infer/infer  
ENV PATH ${INFER_HOME}/bin:${PATH}  

