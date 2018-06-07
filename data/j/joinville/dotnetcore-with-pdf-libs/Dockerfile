FROM microsoft/dotnet:2.0-runtime-deps  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
pdftk \  
ghostscript \  
imagemagick \  
gsfonts \  
&& rm -rf /var/lib/apt/lists/*  

