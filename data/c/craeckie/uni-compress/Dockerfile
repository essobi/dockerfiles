FROM craeckie/uni-base  
  
MAINTAINER Josia <josia-login@rosskopfs.de>  
  
ENV compdir /var/comp  
ENV libdir /usr  
ENV compresslog $logdir/compress.log  
ENV bfgpath /root/bfg-1.12.4.jar  
  
RUN apt-get update && apt-get install -y wget build-essential pkg-config nasm
zlib1g-dev libexpat1-dev libx11-dev libxt-dev libxext-dev openjdk-7-jre  
  
ADD build-gs.sh /etc/my_init.d/50-build-gs.sh  
RUN chmod +x /etc/my_init.d/50-build-gs.sh  
  
ADD init-fonts.sh /root/init-fonts.sh  
RUN chmod +x /root/init-fonts.sh && bash /root/init-fonts.sh  
  
# Add BFG-Repo cleaner  
RUN wget -O $bfgpath
http://repo1.maven.org/maven2/com/madgag/bfg/1.12.4/bfg-1.12.4.jar  
  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
ADD cron /etc/cron.d/compress-cron  
RUN chmod 0744 /etc/cron.d/compress-cron  
  
ADD compress.sh /root/compress.sh  
RUN chmod +x /root/compress.sh

