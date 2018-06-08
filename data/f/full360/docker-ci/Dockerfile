FROM docker:1.11  
  
# set labels for builder  
LABEL build.publish.majorversion="1"  
LABEL build.publish.minorversion="1.11"  
LABEL build.publish.imagebase="docker"  
  
ARG AWSCLI_VER  
ARG NOMAD_VERSION  
ARG NOMAD_SHA256  
  
ENV LANG en_US.UTF-8  
  
# Install required packages  
RUN set -ex \  
&& \  
apk add --no-cache \  
bash \  
ca-certificates \  
curl \  
git \  
gnupg \  
groff \  
less \  
make \  
openssl \  
python \  
py-pip \  
tar \  
unzip  
  
  
# Install the AWS packages, F360 bits and Nomad  
RUN \  
mkdir -p /aws \  
# Install and upgrade Pip  
&& pip install --upgrade pip \  
# Install AWS cli  
&& pip install awscli==${AWSCLI_VER} \  
&& apk --purge -v del py-pip \  
# Add some full 360 bits  
&& mkdir -p /root/.gnupg \  
&& echo "allow-loopback-pinentry" >> /root/.gnupg/gpg-agent.conf \  
&& echo "pinentry-mode loopback" >> /root/.gnupg/gpg.conf \  
&& curl -L -s -o /usr/local/share/ca-certificates/full360-root-ca.crt \  
http://pki.full360.com/full360-root-ca.crt \  
&& update-ca-certificates \  
&& curl -L -s -o nomad.zip
"https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip"
\  
&& echo "${NOMAD_SHA256} *nomad.zip" | sha256sum -c - \  
&& unzip nomad.zip -d /usr/local/bin/ \  
&& rm nomad.zip \  
&& curl -L -s -o /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \  
&& apk add glibc-2.23-r3.apk  
  
COPY nomad-helper.sh environment.sh /usr/local/bin/  

