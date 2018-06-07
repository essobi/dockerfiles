# Base image  
FROM buildpack-deps:xenial-curl  
ENV INFER_VERSION=v0.11.0  
ENV OCAML_VERSION=4.04.0  
# Debian config  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
aspcud \  
autoconf \  
automake \  
gcc \  
g++ \  
git \  
groff-base \  
gradle \  
libc6-dev \  
libgmp-dev \  
libmpc-dev \  
libmpfr-dev \  
m4 \  
make \  
maven \  
ncurses-dev \  
ocaml \  
opam \  
openjdk-8-jdk-headless \  
pkg-config \  
python2.7 \  
rsync \  
unzip \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Download the latest Infer release  
RUN cd /opt && \  
curl -sL \  
https://github.com/facebook/infer/releases/download/${INFER_VERSION}/infer-
linux64-${INFER_VERSION}.tar.xz | \  
tar xJ && \  
rm -f /infer && \  
ln -s ${PWD}/infer-linux64-$INFER_VERSION /infer  
  
# Compile Infer  
RUN opam init --compiler=$OCAML_VERSION -j $(getconf _NPROCESSORS_ONLN || echo
1) --yes && \  
cd /infer && \  
./build-infer.sh --opam-switch $OCAML_VERSION && \  
rm -rf /root/.opam  
  
# Install Infer  
ENV INFER_HOME /infer/infer  
ENV PATH ${INFER_HOME}/bin:${PATH}  
  
# Install dependencies for Android sample  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libc6-dev \  
libc6-i386 \  
lib32z1 \  
lib32stdc++6 && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ANDROID_HOME /opt/android-sdk-linux  
WORKDIR $ANDROID_HOME  
RUN curl -o sdk-tools-linux.zip \  
https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip && \  
unzip sdk-tools-linux.zip && \  
rm sdk-tools-linux.zip  
ENV PATH ${ANDROID_HOME}/tools/bin:${PATH}  
RUN echo "sdk.dir=${ANDROID_HOME}" >
/infer/examples/android_hello/local.properties  
  
# for whalebrew  
LABEL io.whalebrew.name 'infer'  
  
WORKDIR /workdir  
  
ENTRYPOINT ["infer"]  
CMD ["-h"]  

