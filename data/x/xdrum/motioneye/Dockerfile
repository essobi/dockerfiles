FROM ubuntu:14.04  
MAINTAINER Alessio Cassibba (x-drum) <swapon@gmail.com>  
  
RUN echo "deb http://ppa.launchpad.net/mc3man/trusty-media/ubuntu trusty main"
\  
> /etc/apt/sources.list.d/media.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED8E640A \  
&& apt-get update \  
&& apt-get install -y \  
python-tornado \  
python-jinja2 \  
python-imaging \  
motion \  
ffmpeg \  
v4l-utils \  
git  
  
ENV TAG 0.22  
RUN git clone https://github.com/ccrisan/motioneye /motioneye \  
&& cd /motioneye \  
&& git checkout tags/${TAG} \  
&& cp /motioneye/settings_default.py /motioneye/settings.py  
  
VOLUME ["/storage"]  
WORKDIR /motioneye  
  
EXPOSE 8765  
CMD ["/usr/bin/python","/motioneye/motioneye.py"]  

