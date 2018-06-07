# Arch_Vips  
  
FROM openmarble/arch-vips:7.42  
MAINTAINER Andreas Trawöger <atrawog@openmarble.org>  
  
RUN cd /code && \  
curl -LO
https://github.com/DDMAL/diva.js/releases/download/v4.0.0/diva-v4.0.0.tar.gz
&& \  
tar -xvf diva-v4.0.0.tar.gz && \  
ln -sf /usr/sbin/convert /usr/local/bin/convert && \  
ln -sf /usr/bin/kdu_compress /usr/local/bin/kdu_compress

