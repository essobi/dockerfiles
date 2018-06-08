FROM yfix/gulp  
  
MAINTAINER Yuri Vysotskiy (yfix) <yfix.dev@gmail.com>  
  
RUN cd /tmp/ \  
&& apt-get update && apt-get install -y \  
libfontconfig1 \  
\  
&& npm i -g \  
phantomjs-prebuilt \  
\  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf
/usr/{{lib,share}/share/{man,doc,info,gnome/help,cracklib},{lib,lib64}/gconv}  

