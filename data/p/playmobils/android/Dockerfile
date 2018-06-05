  
FROM playmobils/android-ndk:27_14b  
ARG DEBIAN_FRONTEND=noninteractive  
# How to use  
# In order to use it, you need to run it with:  
# docker run -v <path to your source>:/src playmobils/android <file to run>  
# The command above mounts your directory to where the container expects the
source to be and builds it.  
# Install dependencies  
RUN apt-get -qq update && \  
apt-get -qqy install --no-install-recommends \  
gawk \  
bc \  
make \  
zip \  
git &&\  
rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/var/cache/apt/archives/* \  
/var/cache/debconf/*-old  

