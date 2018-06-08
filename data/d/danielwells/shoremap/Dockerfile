FROM tklx/base:0.1.1  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
build-essential \  
libxm4 \  
libmrm4 \  
libuil4 \  
freeglut3-dev \  
libx11-dev \  
libxmu-dev \  
libxi-dev \  
libgl1-mesa-glx \  
libglu1-mesa \  
libglu1-mesa-dev \  
libglfw3-dev \  
libgles2-mesa-dev \  
&& apt-get -f install \  
&& mkdir -p /softwares \  
&& wget
ftp://ftp.gwdg.de/pub/grafik/dislin/linux/i586_64/dislin-11.0.linux.i586_64.deb
-P /softwares \  
&& dpkg -i softwares/dislin-11.0.linux.i586_64.deb \  
&& rm softwares/dislin-11.0.linux.i586_64.deb \  
&& wget
http://mirrors.kernel.org/ubuntu/pool/universe/m/motif/libmotif4_2.3.4-5_amd64.deb
-P /softwares \  
&& dpkg -i /softwares/libmotif4_2.3.4-5_amd64.deb \  
&& rm /softwares/libmotif4_2.3.4-5_amd64.deb \  
&& wget http://bioinfo.mpipz.mpg.de/shoremap/SHOREmap_v3.4.tar.gz -P softwares
\  
&& tar -zxvf softwares/SHOREmap_v3.4.tar.gz --directory softwares/ \  
&& sed -i -e 's/L\/usr\/lib\//L\/usr\/lib\/x86_64-linux-gnu\//g'
softwares/SHOREmap_v3.4/makefile \  
&& export LD_LIBRARY_PATH=/usr/local/dislin/ \  
&& make -C softwares/SHOREmap_v3.4 \  
&& rm /softwares/SHOREmap_v3.4.tar.gz \  
&& mv /softwares/SHOREmap_v3.4/SHOREmap /softwares \  
&& rm -rf /softwares/SHOREmap_v3.4/ \  
&& apt-get purge --auto-remove -y build-essential wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-clean --aggressive  
  
ENV LD_LIBRARY_PATH=/usr/local/dislin/  
ENV PATH $PATH:/softwares/  
  
CMD ["bin/bash"]  
  
  

