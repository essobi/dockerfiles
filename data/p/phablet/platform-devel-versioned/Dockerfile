FROM phablet/platform-devel-base:trusty-oracle-java-6  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
bc \  
lzop \  
mingw32 \  
tofrodos \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  

