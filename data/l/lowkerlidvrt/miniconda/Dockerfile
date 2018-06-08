FROM debian:jessie-slim  
  
MAINTAINER Low Ker Li <lowkerli@diverta.co.jp>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
# Install apt-utils first to prevent delaying package configuration error  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
apt-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
curl \  
ca-certificates \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Tini  
ENV TINI_VERSION v0.13.0  
RUN set -x \  
set -x \  
&& curl -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o
/usr/local/bin/tini \  
&& curl -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" -o
/usr/local/bin/tini.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \  
&& rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini  
  
# Install Miniconda  
ENV MINICONDA_VERSION 3-4.2.12  
RUN echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh \  
&& curl -fSL
https://repo.continuum.io/miniconda/Miniconda${MINICONDA_VERSION}-Linux-x86_64.sh
-o ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
CMD ["/bin/bash"]  

