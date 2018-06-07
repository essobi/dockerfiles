FROM debian:jessie-slim  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libasound2 \  
scratch --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["scratch"]  

