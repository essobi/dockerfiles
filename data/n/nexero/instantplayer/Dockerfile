FROM library/ubuntu:14.04  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends curl  
RUN curl
http://doc.instantreality.org/media/uploads/downloads/2.8.0/InstantReality-
Ubuntu-14.04-x64-2.8.0.38619.deb > /tmp/InstantReality-
Ubuntu-14.04-x64-2.8.0.38619.deb  
RUN apt-get purge -y curl;\  
apt-get autoremove -y  
RUN dpkg -i /tmp/InstantReality-Ubuntu-14.04-x64-2.8.0.38619.deb || exit 0  
RUN apt-get install -y -f --no-install-recommends -d  
RUN apt-get install -y -f --no-install-recommends  
RUN apt-get install --no-install-recommends -y -d libasound2-plugins
libopenal1 zenity  
RUN apt-get install --no-install-recommends -y libasound2-plugins libopenal1
zenity  
  
ENV QT_X11_NO_MITSHM=1  
RUN mkdir -p /etc/openal && \  
echo "drivers=pulse" >> /etc/openal/alsoft.conf  
  
RUN rm -f /tmp/InstantReality-Ubuntu-14.04-x64-2.8.0.38619.deb  
RUN apt-get autoclean -y  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64  
  
ENTRYPOINT zenity --info\  
\--title="InstantPlayer Webinterface URL" \  
\--text="http://$(ip -f inet addr show eth0 | grep -Po 'inet \K[\d.]+'):35668"
&\  
/usr/local/bin/InstantPlayer  
  

