FROM maven:3.2-jdk-8  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y openjfx \  
&& apt-get clean \  
&& rm -f /var/lib/apt/lists/*_dists_*  

