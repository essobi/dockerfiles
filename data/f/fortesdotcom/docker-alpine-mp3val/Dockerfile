FROM alpine  
  
RUN apk add --no-cache g++ make  
  
ENV MP3_VAL_SRC=  
  
RUN mkdir -p /tmp/mp3val && \  
cd /tmp/mp3val && \  
wget -q "http://downloads.sourceforge.net/mp3val/mp3val-0.1.8-src.tar.gz" && \  
tar zxf *.tar.gz -C /tmp/mp3val && \  
cd /tmp/mp3val/mp3val-0.1.8-src && \  
make -f Makefile.linux && \  
mv mp3val /usr/bin/mp3val && \  
cd && \  
rm -rf /tmp/mp3val  
  
CMD [ "mp3val" ]  

