FROM consol/centos-xfce-vnc  
MAINTAINER Jerend Cao "bayonet_c@163.com"  
ENV VNC_RESOLUTION=1360x768  
USER 0  
## Install software  
RUN yum install -y wget ibus ibus-libpinyin cjkuni-ukai-fonts \  
&& yum clean all \  
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.py | python
-c "import sys; main=lambda:sys.stderr.write('Download failed\n');
exec(sys.stdin.read()); main()"  
  
## switch back to default user  
USER 2000  
VOLUME ["/library"]  
EXPOSE 5901 6901 8080  

