FROM webcenter/rancher-alfresco  
MAINTAINER wangmuy@gmail.com  
  
COPY assets/init.py /app/  
  
RUN wget http://downloads.sourceforge.net/wqy/wqy-bitmapfont-0.9.9-0_all.deb
-O /tmp/wqy-bitmapfont-0.9.9-0_all.deb  
RUN dpkg -i /tmp/wqy-bitmapfont-0.9.9-0_all.deb  
RUN wget http://downloads.sourceforge.net/wqy/wqy-zenhei-0.8.38-1.deb -O
/tmp/wqy-zenhei-0.8.38-1.deb  
RUN dpkg -i /tmp/wqy-zenhei-0.8.38-1.deb

