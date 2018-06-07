FROM lolhens/baseimage:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
ENV HAMACHI_VERSION 2.1.0.174  
ENV HAMACHI_ARCH x64  
ENV HAMACHI_NAME logmein-hamachi-$HAMACHI_VERSION-$HAMACHI_ARCH  
ENV HAMACHI_FILE $HAMACHI_NAME.tgz  
ENV HAMACHI_URL https://www.vpn.net/installers/$HAMACHI_FILE  
  
  
COPY ["bin/hamachi.sh", "/tmp/"]  
COPY ["bin/inittun.sh", "/tmp/"]  
  
RUN cd "/tmp" \  
&& curl -LO $HAMACHI_URL \  
&& tar -zxf $HAMACHI_FILE \  
&& mv $HAMACHI_NAME "/usr/local/hamachi/" \  
&& ln -sf "/usr/local/hamachi/hamachid" "/usr/bin/hamachi" \  
&& chmod +x "hamachi.sh" \  
&& mv "hamachi.sh" "/usr/local/hamachi/" \  
&& chmod +x "inittun.sh" \  
&& mv "inittun.sh" "/etc/my_init.d/" \  
&& cleanimage  
  
RUN appfolders add "hamachi/config" "/usr/local/hamachi/config"  
  
WORKDIR /usr/local/hamachi  
CMD ./hamachi.sh  
  
VOLUME /usr/local/appdata/hamachi  

