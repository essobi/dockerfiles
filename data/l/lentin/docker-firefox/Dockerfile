FROM consol/centos-xfce-vnc:latest  
  
ENV VNC_RESOLUTION 1280x720  
  
USER 0  
WORKDIR /usr/local  
RUN yum -y remove firefox \  
&& yum install -y bzip2 \  
&& yum clean all \  
&& wget --content-disposition "https://download.mozilla.org/?product=firefox-
latest&os=linux64&lang=en-US" \  
&& tar xvjf firefox-*.tar.bz2 \  
&& ln -s /usr/local/firefox/firefox /usr/bin/firefox \  
&& rm firefox-*.tar.bz2  
  
USER 1984  

