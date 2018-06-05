FROM ubuntu:xenial  
MAINTAINER sinkerine@gmail.com  
  
RUN apt-get update -y  
RUN apt-get install -y xdg-utils wget python xz-utils  
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.py |
python -c "import sys; main=lambda:sys.stderr.write('Download failed\n');
exec(sys.stdin.read()); main()"  
RUN apt-get clean \  
&& rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
EXPOSE 8080  
RUN ([ -d /opt/calibre ] || mkdir /opt/calibre) \  
&& ([ -d /opt/calibre/library ]) || mkdir /opt/calibre/library  
RUN [ -d /opt/calibre/conf ] || mkdir /opt/calibre/conf  
  
VOLUME ["/opt/calibre/library", "/opt/calibre/conf"]  
ENTRYPOINT ["/usr/bin/calibre-server", "--userdb",
"/opt/calibre/conf/users.sqlite", "/opt/calibre/library"]  

