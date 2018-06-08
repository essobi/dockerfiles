FROM debian:stretch  
MAINTAINER iaroki  
RUN apt-get update && apt-get install -y wget xz-utils gconf2 gconf-service
gvfs-bin libasound2 libcap2 libgconf-2-4 \  
libgnome-keyring-dev libgtk2.0-0 libnotify4 libnss3 libxkbfile1 libxss1
libxtst6 xdg-utils \  
fonts-liberation libgl1-mesa-dri libgl1-mesa-glx \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* && mkdir -p /home/iaroki/PT &&
cd /home/iaroki/PT \  
&& wget https://get.popcorntime.sh/build/Popcorn-Time-0.3.10-Linux-64.tar.xz
&& tar xf Popcorn-Time-0.3.10-Linux-64.tar.xz \  
&& rm -rf Popcorn-Time-0.3.10-Linux-64.tar.xz  
RUN useradd -m -u 1000 -G audio,video iaroki  
COPY asoundrc /home/iaroki/.asoundrc  
USER iaroki  
WORKDIR /home/iaroki/PT  
ENTRYPOINT ["/home/iaroki/PT/Popcorn-Time"]  

