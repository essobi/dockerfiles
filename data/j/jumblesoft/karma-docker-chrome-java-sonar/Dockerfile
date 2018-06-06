FROM atlassian/default-image:latest  
  
RUN apt-get install apt-transport-https -y  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg \--dearmor >
microsoft.gpg && \  
mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \  
sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-trusty-prod trusty main" > /etc/apt/sources.list.d/dotnetdev.list'  
  
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-
cli trusty main" > /etc/apt/sources.list.d/azure-cli.list' && \  
apt-key adv \--keyserver packages.microsoft.com --recv-keys
52E16F86FEE04B979B07E28DB02C46DF417A0893  
  
RUN DEBIAN_FRONTEND="noninteractive" \  
apt-get install make -y \--no-install-recommends && \  
curl https://www.openssl.org/source/openssl-1.0.2o.tar.gz | tar xz && cd
openssl-1.0.2o && ./config && make && make install && \  
ln -sf /usr/local/ssl/bin/openssl `which openssl` && \  
openssl version -v  
  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y \--no-install-recommends \  
chromium-browser \  
azure-cli \  
libgconf-2-4  
  
RUN DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y \  
liblttng-ust0 \  
libstdc++6 \  
dotnet-hostfxr-1.1.0 \  
dotnet-sharedframework-microsoft.netcore.app-1.0.7 \  
dotnet-sharedframework-microsoft.netcore.app-1.1.4 \  
dotnet-dev-1.1.4  
  
ENV CHROME_BIN /usr/bin/chromium-browser  

