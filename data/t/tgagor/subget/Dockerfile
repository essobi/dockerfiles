FROM debian:jessie  
  
MAINTAINER tgagor, https://github.com/tgagor  
  
# Install prerequisites  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y apt-utils \  
&& apt-get install -y git python-pip python-gtk2 python-dbus gettext p7zip-
full \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install python-gettext  
  
RUN git clone https://github.com/webnull/subget.git \  
&& cd subget \  
&& ./setup.py build \  
&& ./setup.py install \  
&& ./setup.py install_data \  
&& ln -s /usr/local/share/subget/ /usr/share/subget \  
&& cd .. \  
&& rm -fr subget  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
  
CMD ["/usr/local/bin/subget"]  

