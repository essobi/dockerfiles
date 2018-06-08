FROM debian:8.7  
MAINTAINER Sho Fuji <pockawoooh@gmail.com>  
  
WORKDIR /work  
  
ENTRYPOINT ["/work/font-patcher"]  
  
  
ENV FONTFORGE_VERSION=20161005 \  
NERDFONTS_VERSION=1.0.0  
  
RUN apt-get update && \  
# Install dependencies  
apt-get install -y \  
autotools-dev libjpeg-dev libtiff5-dev \  
libpng-dev libgif-dev libxt-dev libfreetype6-dev \  
autoconf automake libtool libltdl7-dev \  
libxml2-dev libuninameslist-dev libspiro-dev \  
python-dev libpango1.0-dev libcairo2-dev \  
chrpath git && \  
# Install fontforge  
TMP=$(mktemp -d) && \  
cd ${TMP} && \  
curl -LO
https://github.com/fontforge/fontforge/releases/download/${FONTFORGE_VERSION}/fontforge-${FONTFORGE_VERSION}.tar.gz
&& \  
tar -axf fontforge-${FONTFORGE_VERSION}.tar.gz && \  
cd fontforge-${FONTFORGE_VERSION} && \  
./bootstrap && \  
./configure && \  
make && \  
make install && \  
ldconfig &&\  
rm -rf ${TMP} && \  
# Install nerd-fonts  
cd /work && \  
curl -LO https://github.com/ryanoasis/nerd-
fonts/archive/v${NERDFONTS_VERSION}.tar.gz && \  
tar -axf v${NERDFONTS_VERSION}.tar.gz --strip-components 1 && \  
rm v${NERDFONTS_VERSION}.tar.gz && \  
ls -la  

