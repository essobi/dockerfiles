FROM bradjones/dotnet-ide:latest  
LABEL maintainer "brad@bjc.id.au"  
  
# Download and extract rider  
RUN cd /opt && \  
curl -L
https://data.services.jetbrains.com/products/download?code=RD\&platform=linux
| \  
tar xz && \  
mv `ls` rider

