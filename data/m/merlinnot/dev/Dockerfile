# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers. This is development package and it is meant to  
# be latest and greatest.  
###############################################################################  
# CORE  
FROM phusion/baseimage:latest  
  
MAINTAINER Natan Sągol <m@merlinnot.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Update image  
RUN apt-get -qq update && apt-get -qq upgrade -y -o \  
Dpkg::Options::="--force-confold"  
  
# Install essential tools  
RUN apt-get install -y --no-install-recommends vim nano git wget curl unzip  
# Add insecure Vagrant key  
RUN rm -f /etc/service/sshd/down && /usr/sbin/enable_insecure_key  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
RUN mkdir -p /root/.ssh && curl -sL \  
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub \  
> /root/.ssh/authorized_keys  
  
###############################################################################  
# LANGUAGES, LIBRARIES & LANGUAGE-SPECIFIC TOOLS  
# Installing Python  
RUN apt-get install -y --no-install-recommends \  
python \  
python3 \  
python-dev \  
python3-dev \  
python-pip \  
python3-pip \  
libpython-all-dev \  
libpython3-all-dev \  
python-setuptools \  
python3-setuptools  
  
# Install basic C/C++ stack  
RUN apt-get install -y --no-install-recommends \  
build-essential \  
clang  
RUN BOOST_MAJOR=1 && \  
BOOST_MINOR=62 && \  
BOOST_PATCH=0 && \  
BOOST_BASE_URL="http://sourceforge.net/projects/boost/files/boost/" && \  
BOOST_VERSION_DIR="${BOOST_MAJOR}.${BOOST_MINOR}.${BOOST_PATCH}/" && \  
BOOST_PKG="boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_PATCH}.tar.bz2" && \  
wget -c \  
"${BOOST_BASE_URL}${BOOST_VERSION_DIR}${BOOST_PKG}/download" \  
\--directory-prefix=/tmp/boost/ && \  
mkdir /tmp/boost/extracted && \  
tar -xf /tmp/boost/download -C /tmp/boost/extracted/ && \  
cd /tmp/boost/extracted/boost_1_${BOOST_MINOR}_0 && \  
./bootstrap.sh --prefix=/usr/local/ && \  
./b2 -d0 install && \  
rm -r /tmp/boost  
  
# Install basic Haskell stack  
RUN apt-get install -y --no-install-recommends libtinfo-dev  
ENV PATH="${HOME}/.local/bin:${PATH}"  
RUN curl -sSLq https://get.haskellstack.org/ | sh  
RUN stack setup  
RUN stack install \  
apply-refact \  
hlint \  
stylish-haskell \  
hasktags \  
hoogle \  
intero \  
hindent  
  
# Install basic Go stack  
RUN GO_VERSION="1.7.3" && \  
GO_BASE_URL="https://storage.googleapis.com/golang/" && \  
wget -q ${GO_BASE_URL}go${GO_VERSION}.linux-amd64.tar.gz && \  
tar -xf go${GO_VERSION}.linux-amd64.tar.gz && \  
mv go /usr/local && \  
rm go${GO_VERSION}.linux-amd64.tar.gz  
RUN mkdir ${HOME}/.go  
ENV GOROOT=/usr/local/go  
ENV GOPATH=${HOME}/.go  
ENV PATH="${GOPATH}/bin:${GOROOT}/bin:${PATH}"  
RUN go get -u \  
github.com/nsf/gocode \  
github.com/rogpeppe/godef \  
golang.org/x/tools/cmd/guru \  
golang.org/x/tools/cmd/gorename \  
golang.org/x/tools/cmd/goimports \  
github.com/alecthomas/gometalinter && \  
gometalinter --install  
  
RUN mkdir -p "${GOPATH}/bin" && curl https://glide.sh/get | sh  
  
# Install Google App Engine SDK for Go  
ENV GO_APPENGINE_VERSION="1.9.46"  
ENV GO_APPENGINE_URL="https://storage.googleapis.com/appengine-sdks/featured/"  
ENV
GO_APPENGINE_FILE="go_appengine_sdk_linux_amd64-${GO_APPENGINE_VERSION}.zip"  
RUN wget -q \  
"${GO_APPENGINE_URL}${GO_APPENGINE_FILE}" \  
-O /tmp/sdk.zip  
RUN unzip -qq /tmp/sdk.zip -d "${HOME}" && \  
rm /tmp/sdk.zip && \  
mv "${HOME}/go_appengine" "${HOME}/.go_appengine"  
ENV PATH="${PATH}:/usr/local/.go_appengine"  
RUN go get google.golang.org/appengine  
  
# Install Node  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash && \  
apt-get install -y --no-install-recommends nodejs  
RUN npm install -g \  
tern \  
js-beautify \  
eslint  
  
# Install Yarn  
RUN curl https://dl.yarnpkg.com/debian/pubkey.gpg | \  
apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | \  
tee /etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install yarn  
  
###############################################################################  
# COMMAND-LINE FRAMEWORKS, TOOLKITS, EDITORS $ OPTIONS  
# Install spacemacs  
RUN apt-get install -y --no-install-recommends emacs  
RUN git clone https://github.com/syl20bnr/spacemacs ~/.emacs.d  
COPY .spacemacs /root/.spacemacs  
RUN emacs -nw -batch -u "${UNAME}" -q -kill  
  
# Install The Fuck  
# See .bash_ext for alias configuration  
RUN pip3 install thefuck  
  
# Install gcloud toolkit  
RUN apt-get install -y --no-install-recommends unzip && \  
wget -q https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& \  
unzip -q google-cloud-sdk.zip && \  
mv ./google-cloud-sdk ${HOME}/.google-cloud-sdk && \  
rm -r google-cloud-sdk* && \  
${HOME}/.google-cloud-sdk/install.sh \  
\--usage-reporting=true \  
\--path-update=true \  
\--bash-completion=true \  
\--rc-path=${HOME}/.profile \  
\--additional-components \  
app-engine-python \  
app \  
kubectl \  
alpha \  
beta \  
gcd-emulator \  
pubsub-emulator \  
cloud-datastore-emulator \  
app-engine-go \  
bigtable  
  
# Install ngrok  
RUN apt-get install ngrok-client  
  
# Apply custom bash settings  
COPY .bash_ext /root/.bash_ext  
RUN echo "source $HOME/.bash_ext" >> $HOME/.profile  
  
###############################################################################  
# SHRINKING IMAGE  
# Clean up APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

