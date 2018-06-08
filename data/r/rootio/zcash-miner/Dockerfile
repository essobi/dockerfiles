FROM ubuntu:latest  
  
MAINTAINER David Routhieau "rootio@protonmail.com"  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y \  
build-essential \  
pkg-config \  
libc6-dev \  
m4 \  
g++-multilib \  
autoconf \  
libtool \  
ncurses-dev \  
unzip \  
git \  
python \  
zlib1g-dev \  
wget \  
bsdmainutils \  
automake \  
apg  
  
RUN mkdir -p /root/.zcash  
  
COPY ./zcash.conf /root/.zcash/zcash.conf  
  
RUN sed -i -e "s/SECRET/$(apg -MCLN -m 24 -n 1)/g" /root/.zcash/zcash.conf  
  
RUN git clone https://github.com/zcash/zcash.git /srv/zcash  
  
WORKDIR /srv/zcash  
  
RUN git checkout v1.0.13  
  
RUN ./zcutil/fetch-params.sh  
  
RUN ./zcutil/build.sh -j$(nproc)  
  
CMD ["./src/zcashd", "-daemon"]  
  
EXPOSE 8233  
EXPOSE 18233  

