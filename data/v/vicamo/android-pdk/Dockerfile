FROM vicamo/openjdk:xenial-7-jdk  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
adb \  
android-tools-fsutils \  
bison \  
build-essential \  
ccache \  
curl \  
fastboot \  
file \  
flex \  
g++-multilib \  
git \  
gnupg \  
gperf \  
less \  
libgl1-mesa-glx \  
libgl1-mesa-glx:i386 \  
libxml2-utils \  
make \  
telnet \  
unzip \  
wget \  
zip \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  
  
RUN wget -nv -O /usr/bin/repo https://storage.googleapis.com/git-repo-
downloads/repo \  
&& chmod a+x /usr/bin/repo  
  
ENV USE_CCACHE 1  

