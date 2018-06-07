FROM jenkins  
  
USER root  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install -y libncurses5:i386 libstdc++6:i386 zlib1g:i386 rpm
fakeroot build-essential nodejs expect  
RUN mkdir /android && chown jenkins /android  
  
RUN rm /bin/sh \  
&& ln -s bash /bin/sh  
  
USER jenkins  

