FROM ubuntu:xenial  
  
RUN apt-get update  
  
RUN apt-get install -y --no-install-recommends ca-certificates python3
python3-pip gnuplot-nox curl xmlstarlet  
  
RUN apt-get download gupnp-tools libgssdp-1.0-3 libglib2.0-0 libsoup2.4-1
libffi6 libxml2 libsqlite3-0 libicu55  
  
RUN dpkg --force-all -i *.deb  
  
ENV SPEEDTEST_VERSION 1.0.2  
RUN pip3 install speedtest-cli==$SPEEDTEST_VERSION  
  
ADD cmd.sh /  
  
ADD *.xml /  
  
ADD speedtest.gnu /  
  
ADD data/ /data  
  
VOLUME /data  
  
ENV GSSDP_INTERFACE="wlp4s0"  
CMD ["/cmd.sh"]  

