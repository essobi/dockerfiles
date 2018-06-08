FROM navicore/naviron-chezscheme  
  
MAINTAINER Ed Sweeney <ed@onextent.com>  
  
WORKDIR /root  
  
RUN git clone https://github.com/vyzo/gerbil.git && cd gerbil/src &&
PATH=$PATH:/usr/local/Gambit/bin ./build.sh \  
&& ln -s /root/gerbil/bin/gxc /usr/local/bin/gxc \  
&& ln -s /root/gerbil/bin/gxi /usr/local/bin/gxi \  
&& ln -s /root/gerbil/bin/gxi-build-script /usr/local/bin/gxi-build-script \  
&& ln -s /root/gerbil/bin/gxi-script /usr/local/bin/gxi-script \  
&& ln -s /root/gerbil/bin/gxprof /usr/local/bin/gxprof  
  

