FROM elixir:1.4.5  
# Version: 2017-07-25 01  
WORKDIR /tmp  
  
RUN wget -q http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz \  
&& tar xJf /tmp/ffmpeg-release-64bit-static.tar.xz -C /tmp \  
&& mv /tmp/ffmpeg-3.3.2-64bit-static/ffprobe /usr/local/bin/ \  
&& mv /tmp/ffmpeg-3.3.2-64bit-static/ffmpeg /usr/local/bin/ \  
&& rm -rf /tmp/ffmpeg*  
  
CMD ["iex"]  

