FROM microsoft/dotnet:2.0-sdk  
  
WORKDIR /app/src  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
netcat \  
&& rm -rf /var/lib/apt/lists/*  

