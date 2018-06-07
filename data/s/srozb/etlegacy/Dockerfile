FROM ubuntu:14.04  
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>  
  
ENV ETL_PATH /root/etlegacy  
  
RUN apt-get update -y && apt-get install -y wget  
RUN wget -O etlegacy-2.74.tar.gz https://www.etlegacy.com/download/file/74 \  
&& tar -xzf etlegacy-2.74.tar.gz && rm -f etlegacy-2.74.tar.gz \  
&& mv etlegacy-v2.74-x86_64 $ETL_PATH  
  
#ENV PAK_MIRROR http.kernwaffe.de/et/etmain  
ENV PAK_MIRROR fd.zabijaka.pl/s8441/etmain  
  
WORKDIR $ETL_PATH/etmain  
RUN wget http://$PAK_MIRROR/pak0.pk3 \  
&& wget http://$PAK_MIRROR/pak1.pk3 \  
&& wget http://$PAK_MIRROR/pak2.pk3 \  
&& wget http://$PAK_MIRROR/mp_bin.pk3  
  
WORKDIR $ETL_PATH  
  

