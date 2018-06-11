FROM jordi/golang-run  
MAINTAINER wolfitem <wei.wu86@hotmail.com>  
  
# Download LiteIDE prerequisites  
RUN apt-get -y install make gdb libqt4-dev  
  
# LiteIDE  
RUN wget
http://heanet.dl.sourceforge.net/project/liteide/X27.2.1/liteidex27.2.1.linux-64-qt4.tar.bz2
-q -O - | bunzip2 -c | tar -xf - -C /usr/local  
ADD linux64.env /usr/local/liteide/share/liteide/liteenv/linux64.env  
ADD liteide.ini /.config/liteide/liteide.ini  
ADD system.env /usr/local/liteide/share/liteide/liteenv/system.env  
  
# X11  
# This is optional: RUN apt-get install -y xterm gnome-terminal  
RUN apt-get install -y xterm  
  
# install language (zh-cn)  
RUN apt-get install -y language-pack-gnome-zh-hans  
RUN apt-get install -y ttf-wqy-zenhei  
  
# 处理中文问题  
ENV LANG=zh_CN.utf-8  
ENV GOROOT=/usr/local/go  
ENV GOPATH=/go/gopath  
  
# shell launch  
ENV QT_X11_NO_MITSHM 1  
CMD ["/usr/local/liteide/bin/liteide"]  
  

