FROM microsoft/dotnet:sdk  
  
MAINTAINER calvintam236 <calvintam236@users.noreply.github.com>  
LABEL description="MiningCore in Docker. This is a mining pool software."  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get -y \--no-install-recommends install ca-certificates curl build-
essential cmake libboost-all-dev libsodium-dev libssl-dev pkg-config \  
&& curl -L -O https://github.com/coinfoundry/miningcore/archive/0.24.tar.gz \  
&& tar -xvf 0.24.tar.gz \  
&& rm 0.24.tar.gz \  
&& cd miningcore-0.24/src/MiningCore \  
&& chmod +x ./linux-build.sh \  
&& ./linux-build.sh \  
&& mkdir /usr/local/miningcore \  
&& cp -r ../../build/* /usr/local/miningcore \  
&& cd ../../.. \  
&& rm -rf miningcore-0.24 \  
&& apt-get -y remove ca-certificates curl build-essential cmake libboost-all-
dev libsodium-dev libssl-dev pkg-config \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& apt-get -y \--no-install-recommends install libboost-date-time1.62.0
libboost-system1.62.0 libsodium18 libssl1.1 \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ENTRYPOINT ["dotnet", "/usr/local/miningcore/MiningCore.dll"]  

