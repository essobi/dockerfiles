# Docker file for development environment  
FROM ubuntu:17.04  
RUN \  
apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y \  
apt-utils software-properties-common \  
python-software-properties \  
build-essential \  
git curl htop man unzip vim wget \  
emacs \  
python python3.6 python3.6-dev python3-pip virtualenvwrapper \  
golang-1.8-go \  
libpng-dev pkg-config \  
&& pip3 install flake8 flake8-mypy  
  
COPY libpng12.deb /tmp/libpng12.deb  
ADD llvm.list /etc/apt/sources.list.d/llvm.list  
ADD llvm.pub.gpg /root/llvm.pub.gpg  
  
# Install Java.  
RUN apt-add-repository ppa:webupd8team/java -y \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java8-installer \  
&& dpkg -i /tmp/libpng12.deb \  
&& rm /tmp/libpng12.deb \  
&& curl -LO
"https://github.com/bazelbuild/bazel/releases/download/0.7.0/bazel_0.7.0-linux-x86_64.deb"
\  
&& dpkg -i bazel_*.deb \  
&& rm -f bazel_*.deb \  
&& apt-key add /root/llvm.pub.gpg \  
&& rm -f /root/llvm.pub.gpg \  
&& apt-get update \  
&& apt-get install -y bazel clang-5.0 clang-format-5.0 llvm-5.0 lldb-5.0  
  
# Install gcloud SDK  
ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
ENV HOME /root  
WORKDIR /root  
RUN apt-get update -y \  
&& apt-get install -y jq \  
&& curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt  
  
RUN gcloud components install kubectl \  
&& gcloud components install docker-credential-gcr \  
&& docker-credential-gcr configure-docker  
  
# Install docker.  
RUN apt-get install -y docker.io \  
&& update-rc.d docker enable  
  
ARG arc_install_path=/opt/phabricator  
WORKDIR ${arc_install_path}  
# Install arc.  
RUN apt-get install -y php php-curl \  
&& git clone https://github.com/phacility/libphutil.git \  
&& git clone https://github.com/phacility/arcanist.git  
ENV PATH /opt/phabricator/arcanist/bin:$PATH  
  
# Bazel options to run inside of Docker.  
COPY bazelrc /etc/bazel.bazelrc  
  
# Install node.  
WORKDIR /opt  
RUN wget https://nodejs.org/dist/v6.10.3/node-v6.10.3-linux-x64.tar.xz \  
&& tar xf node-v6.10.3-linux-x64.tar.xz \  
&& rm node-v6.10.3-linux-x64.tar.xz  
ENV PATH /opt/node-v6.10.3-linux-x64/bin:$PATH  
  
# Install npm packages.  
RUN npm install -g tslint@5.2.0 typescript@2.3.2 yarn@0.23.4 webpack@2.4.1
jshint@2.9.4 jest@20.0.3  
  
# Setup compiler  
ENV CC=/usr/bin/clang  
ENV CXX=/usr/bin/clang++  
# Fix a missing path in the clang config.  
ENV CPLUS_INCLUDE_PATH=/usr/lib/llvm-5.0/lib/clang/5.0.1/include  
RUN update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 100
\  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-5.0
100 \  
&& update-alternatives --install /usr/bin/clang-format clang-format
/usr/bin/clang-format-5.0 100  
  
RUN wget http://www.imagemagick.org/download/ImageMagick.tar.gz \  
&& tar -xvf ImageMagick.tar.gz \  
&& cd ImageMagick-7.* \  
&& ./configure \  
&& make -j4 \  
&& make install \  
&& ldconfig /usr/local/lib  
  
# Set up Go environment.  
ENV GOPATH /axon  
ENV PATH $GOPATH/bin:/usr/lib/go-1.8/bin:$PATH  
  
# We expect the source code to be mounted at /axon/src/github.com/axonmi/axon.  
WORKDIR /axon  
RUN mkdir src bin  
ADD https://storage.googleapis.com/axon-artifacts/gazelle-snapshot-20171130
/axon/bin/gazelle  
RUN apt-get install -y golang-glide \  
&& go get -u github.com/golang/lint/golint \  
&& go get -u golang.org/x/tools/cmd/goimports \  
&& mkdir -p /axon/src/github.com/axonmi/axon \  
&& chmod +rx /axon/bin/gazelle  
  
WORKDIR /axon/src/github.com/axonmi/axon  
CMD ["/bin/bash"]  

