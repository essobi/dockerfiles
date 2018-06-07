#docker pull pivotalgreenhouse/ci  
FROM ruby:2.3.3  
#ENV PACKER_URL
"https://releases.hashicorp.com/packer/0.12.2/packer_0.12.2_linux_amd64.zip"  
ENV PACKER_URL "https://s3.amazonaws.com/windows-bosh-temp/packer-fork-
latest.zip"  
RUN apt-get update -qq && \  
apt-get install -qqy --no-install-recommends apt-transport-https && rm -rf
/var/lib/apt/lists/*  
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-jessie main" |
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update -qq && \  
apt-get install -qqy --no-install-recommends \  
apt-utils \  
build-essential \  
ca-certificates \  
cmake \  
curl \  
freerdp-x11 \  
g++ \  
gcc \  
git \  
google-cloud-sdk \  
libc6-dev \  
libpopt-dev \  
lsb-release \  
make \  
mingw-w64 \  
nano \  
pkg-config \  
python-all \  
python-dev \  
python-pip \  
rlwrap \  
rsync \  
unzip \  
vim \  
wget \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget ${PACKER_URL} -O packer.zip  
RUN unzip packer.zip && mv packer /usr/local/bin/packer && rm packer.zip  
  
RUN gem install bundler  
  
# bosh Golang CLI  
RUN version_number=$(curl 'https://github.com/cloudfoundry/bosh-
cli/releases/latest' 2>&1 | egrep -o '([0-9]+\\.[0-9]+\\.[0-9]+)') && \  
curl "https://s3.amazonaws.com/bosh-cli-artifacts/bosh-
cli-${version_number}-linux-amd64" -o /usr/local/bin/bosh && \  
chmod 755 /usr/local/bin/bosh  
  
# azure CLI  
# see https://github.com/Azure/azure-cli-docker/blob/master/0.10.0/Dockerfile  
ENV AZURE_CLI_VERSION "0.10.0"  
ENV NODEJS_APT_ROOT "node_4.x"  
ENV NODEJS_VERSION "4.2.4"  
RUN curl
https://deb.nodesource.com/${NODEJS_APT_ROOT}/pool/main/n/nodejs/nodejs_${NODEJS_VERSION}-1nodesource1~jessie1_amd64.deb
> node.deb && \  
dpkg -i node.deb && \  
rm node.deb && \  
npm install --global azure-cli@${AZURE_CLI_VERSION} && \  
azure --completion >> ~/azure.completion.sh && \  
echo 'source ~/azure.completion.sh' >> ~/.bashrc && \  
azure  
  
RUN azure config mode arm  
  
RUN wget -q https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
-O /usr/local/bin/jq && chmod +x /usr/local/bin/jq  
  
RUN pip install awscli  
RUN gem install aws-sdk  
RUN gem install azure_mgmt_resources  
  
ENV GOLANG_VERSION 1.9.2  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
de874549d9a8d8d8062be05808509c09a88a248e77ec14eb77453530829ac02b  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 755 "$GOPATH/bin"  
  
#install CF CLI  
RUN wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add -  
RUN echo "deb http://packages.cloudfoundry.org/debian stable main" | tee
/etc/apt/sources.list.d/cloudfoundry-cli.list  
RUN apt-get update  
RUN apt-get install cf-cli  
  

