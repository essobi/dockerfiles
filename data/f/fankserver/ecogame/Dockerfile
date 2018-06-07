FROM debian:9  
  
LABEL maintainer "Florian Kinder <florian.kinder@fankserver.com>"  
  
RUN apt-get update -qq && \  
apt-get install -qqy gnupg2 && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian alpha-stretch main" |
tee /etc/apt/sources.list.d/mono-official-alpha.list && \  
apt-get update -qq && \  
apt-get install -qqy wget unzip ca-certificates mono-complete
referenceassemblies-pcl ca-certificates-mono mono-xsp4 && \  
rm -rf /var/lib/apt/lists/* && \  
wget https://s3-us-west-2.amazonaws.com/eco-
releases/EcoServer_v0.5.6.1-alpha.zip -O /tmp/EcoServer.zip && \  
unzip /tmp/EcoServer.zip -d /eco/ && \  
rm /tmp/EcoServer.zip  
  
EXPOSE 2999 3000 3001  
  
VOLUME ["/eco/Storage", "/eco/Configs"]  
  
WORKDIR /eco  

