FROM ubuntu:16.04  
#MAINTAINER nick.humrich@canopytax.com  
# Set the NODEJS_VERSION below to change the node version  
ENV NODEJS_VERSION=8.11.2  
ENV DEBIAN_FRONTEND=noninteractive  
  
  
COPY woff-code-latest.zip /tmp/  
# Make sure python, awscli, fontcustom, and git are all installed.  
RUN apt -y update && \  
apt install -y python python-pip python-dev wget unzip git build-essential
zlib1g-dev ruby-full rubygems fontforge apt-transport-https ca-certificates &&
\  
pip install awscli  
  
RUN git clone https://github.com/bramstein/sfnt2woff-zopfli.git sfnt2woff-
zopfli && cd sfnt2woff-zopfli && make && mv sfnt2woff-zopfli
/usr/local/bin/sfnt2woff && \  
git clone --recursive https://github.com/google/woff2.git && cd woff2 && make
clean all && mv woff2_compress /usr/local/bin/ && mv woff2_decompress
/usr/local/bin/ && \  
gem install fontcustom && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /www  
  
# Now install node/npm.  
RUN apt update && apt install bzip2 curl build-essential libssl-dev
libfontconfig1 -y && \  
curl -SLO
"https://nodejs.org/download/release/v$NODEJS_VERSION/node-v$NODEJS_VERSION-
linux-x64.tar.gz" && \  
tar -xzf "node-v$NODEJS_VERSION-linux-x64.tar.gz" -C /usr/local --strip-
components=1 && \  
npm install -g npm && \  
npm set progress=false \  
apt remove --purge -y libssl-dev && \  
apt autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
# install yarn (yarnpkg.com)  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt update && apt install --no-install-recommends yarn -y && \  
rm -rf /var/lib/apt/lists/*  

