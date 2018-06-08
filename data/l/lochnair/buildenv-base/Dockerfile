FROM alpine:3.7  
# Install build dependencies  
RUN apk add --no-cache \  
\--update-cache \  
autoconf \  
automake \  
bc \  
bison \  
build-base \  
coreutils \  
curl \  
file \  
flex \  
gawk \  
git \  
gmp-dev \  
libtool \  
linux-headers \  
mpc1-dev \  
mpfr-dev \  
shadow \  
su-exec \  
texinfo \  
wget  
  
# Add user and set entrypoint  
RUN useradd -m -U -s /bin/sh -u 1234 user  

