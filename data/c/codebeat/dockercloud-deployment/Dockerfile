FROM alpine:latest  
  
# Install Docker Cloud toolchain.  
RUN apk add --update curl \  
python \  
python-dev \  
py-pip \  
zip \  
&& pip install --upgrade pip \  
&& pip install docker-cloud pyyaml  
  
# Install Codeship Jet toolchain.  
ENV JET_VERSION=1.13.4  
ENV JET_TARBALL="jet-linux_amd64_${JET_VERSION}.tar.gz"  
RUN cd /tmp \  
&& curl -SLO "https://s3.amazonaws.com/codeship-jet-
releases/${JET_VERSION}/${JET_TARBALL}" \  
&& tar -xz -f $JET_TARBALL -C /usr/bin \  
&& rm $JET_TARBALL  
  
COPY scripts/ /usr/bin  
WORKDIR /workbench  

