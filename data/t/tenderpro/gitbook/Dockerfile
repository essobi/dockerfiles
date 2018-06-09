FROM tenderpro/nodejs:0.5  
MAINTAINER Alexey Kovrizhkin <lekovr+tpro@gmail.com>  
  
ENV DOCKERFILE_VERSION 171019  
#
-------------------------------------------------------------------------------  
# Gitbook & libs  
RUN apt-get update && apt-get install -y \  
xz-utils wget xvfb imagemagick libgl1-mesa-glx libxcomposite1 locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias
ru_RU.UTF-8  
  
ENV LANG ru_RU.utf8  
  
# GitBook from https://www.gitbook.com/  
RUN npm install gitbook-cli -g  
  
# Calibre from https://calibre-ebook.com/  
ENV CALIBRE_VER 3.9.0  
RUN wget -nv -O calibre-x86_64.txz https://download.calibre-
ebook.com/$CALIBRE_VER/calibre-$CALIBRE_VER-x86_64.txz \  
&& mkdir -p /opt/calibre && rm -rf /opt/calibre/* \  
&& tar xvf calibre-x86_64.txz -C /opt/calibre > /dev/null \  
&& rm calibre-x86_64.txz \  
&& /opt/calibre/calibre_postinstall  
  
RUN gosu op gitbook fetch  

