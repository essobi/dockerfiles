FROM buildpack-deps:xenial  
MAINTAINER roman-kozachenko  
  
RUN apt-get update -y \  
&& apt-get install -y apt-transport-https \  
&& echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-
release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys 417A0893
\  
&& apt-get update -y \  
&& apt-get install -y dotnet-dev-1.0.4 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Trigger the population of the local package cache  
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1  
RUN mkdir warmup \  
&& cd warmup \  
&& dotnet new mvc --framework netcoreapp1.1 \  
&& dotnet restore \  
&& cd .. \  
&& rm -rf warmup \  
&& rm -rf /tmp/NuGetScratch  

