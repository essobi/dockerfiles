FROM gfjardim/cups  
MAINTAINER Sebastian Schneider <mail@sesc.eu>  
  
RUN wget -O /tmp/mccgdi-2.0.9-x86_64.tar.gz \  
http://cs.psn-
web.net/support/fax/common/file/Linux_PrnDriver/Driver_Install_files/mccgdi-2.0.9-x86_64.tar.gz
\  
&& tar -xvzf /tmp/mccgdi-2.0.9-x86_64.tar.gz \  
&& cd mccgdi-2.0.9-x86_64 \  
&& ./install-driver \  
&& ln -s /usr/lib/x86_64-linux-gnu/libgs.so.9 /usr/lib/libgs.so  

