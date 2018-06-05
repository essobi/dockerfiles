FROM debian:jessie-slim  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
blender --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
ENTRYPOINT [ "blender" ]  

