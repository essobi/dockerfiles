FROM rancher/convoy-agent:v0.9.0  
  
COPY launch /  
  
RUN apt-get update \  
&& apt-get install util-linux -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /convoy:$PATH  

