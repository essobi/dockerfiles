FROM ubuntu  
MAINTAINER Josh Wheeler <joshwheeler@mantlepro.com>  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository ppa:stebbins/handbrake-releases && \  
add-apt-repository multiverse && \  
apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y handbrake-cli libdvd-pkg
libcdio-utils  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure libdvd-pkg  
ENTRYPOINT ["HandBrakeCLI"]  
CMD ["-i", "/dev/sr0", "-o", "/media/movie.m4v", "--main-feature", "--cfr",
"-e", "x264", "-q", "17", "-a", "1,1", "-E", "faac,copy:ac3", "-B", "256,256",
"-6", "dpl2,none", "-R", "Auto,Auto", "--audio-copy-mask",
"aac,ac3,dtshd,dts,mp3", "--audio-fallback", "ffac3", "-f", "av_mp4", "--
decomb", "--modulus", "2", "-m", "--x264-preset", "slower", "--x264-tune",
"film", "--h264-level", "4.0"]  

