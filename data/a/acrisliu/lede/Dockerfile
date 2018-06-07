FROM ubuntu:xenial  
  
MAINTAINER Acris Liu "acrisliu@gmail.com"  
ENV LEDE_VERSION=v17.01.4  
RUN set -ex \  
&& apt update \  
&& apt install --no-install-recommends --no-install-suggests -y \  
subversion g++ zlib1g-dev build-essential git python rsync man-db \  
libncurses5-dev gawk gettext unzip file libssl-dev wget openssl ca-
certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& useradd -m -s /bin/bash lede  
  
USER lede  
  
RUN set -ex \  
&& cd /home/lede \  
&& git clone -b $LEDE_VERSION https://git.lede-project.org/source.git lede \  
&& cd lede \  
&& ./scripts/feeds update -a \  
&& ./scripts/feeds install -a  
  
WORKDIR /home/lede/lede  
  
CMD ["/bin/bash"]  

