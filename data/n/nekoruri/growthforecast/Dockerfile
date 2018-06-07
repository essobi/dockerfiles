FROM ubuntu:trusty  
  
MAINTAINER NAKAYAMA Masahiro <aki@nekoruri.jp>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cpanminus  
RUN DEBIAN_FRONTEND=noninteractive apt-get build-dep -y rrdtool  
RUN cpanm -n GrowthForecast  
  
RUN useradd -m -s /bin/bash growthforecast  
RUN mkdir -p -m755 /data/growthforecast  
RUN chown growthforecast:growthforecast /data/growthforecast  
  
ENTRYPOINT [ "/usr/local/bin/growthforecast.pl" ]  
CMD [ "--data-dir", "/data/growthforecast" ]  
EXPOSE 5125  

