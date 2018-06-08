FROM chiguri/platex  
LABEL maintainer "Sosuke Moriguchi"  
ENV PANDOC_VERSION=1.19.2.1  
ENV DEBIAN_FRONTEND=noninteractive  
RUN wget
https://github.com/jgm/pandoc/releases/download/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-amd64.deb
&& \  
dpkg -i pandoc-$PANDOC_VERSION-1-amd64.deb && \  
rm pandoc-$PANDOC_VERSION-1-amd64.deb  
  

