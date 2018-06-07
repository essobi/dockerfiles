FROM zburgermeiszter/usermode-alpine:3.3  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
USER root  
  
RUN apk add mono xdotool libgdiplus --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ && \  
apk add --no-cache ttf-dejavu && \  
ln /usr/lib/libgdiplus.so.0 /usr/lib/libgdiplus.so  
  
USER user  
RUN wget
http://downloads.sourceforge.net/project/keepass/KeePass%202.x/2.33/KeePass-2.33.zip
-O keepass.zip && \  
echo "b98fd89516f14b4afa66f7c839700293 keepass.zip" | md5sum -sc && \  
mkdir .keepass && \  
unzip keepass.zip -d .keepass && \  
rm keepass.zip  
  
ADD ./plugins /home/user/.keepass/plugins  
  
ENV HOME /home/user/keepass  
  
ENTRYPOINT ["/bin/sh","-c","/usr/bin/mono /home/user/.keepass/KeePass.exe"]

