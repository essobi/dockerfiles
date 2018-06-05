FROM ubuntu  
RUN dpkg --add-architecture i386  
  
RUN apt-get update -y && \  
apt-get install -y software-properties-common ssh git && add-apt-repository -y
ppa:ubuntu-wine/ppa && \  
apt-get update -y && \  
apt-get install --no-install-recommends -y wine1.8  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && \  
apt-get install --no-install-recommends -y mono-devel ca-certificates-mono  
  
RUN apt-get install -y curl libc6 libcurl3 zlib1g  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
  
RUN apt-get purge -y curl software-properties-common && apt-get autoclean -y  
  
RUN node -v  
RUN npm -v  

