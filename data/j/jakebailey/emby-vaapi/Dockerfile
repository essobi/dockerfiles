FROM dperson/emby:latest  
  
# 91 on Arch Linux.  
ARG VIDEO_GID="91"  
  
RUN rm /bin/ffmpeg /bin/ffprobe \  
&& apt-get update \  
&& apt-get install -y \  
ffmpeg \  
libva1 \  
vainfo \  
i965-va-driver \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupmod -g ${VIDEO_GID} video \  
&& usermod -a -G video emby  

