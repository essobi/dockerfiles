FROM java:8-jre  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install wget supervisor  
  
ENV JAR_FILE=https://circle-
artifacts.com/gh/DragonetMC/DragonProxy/278/artifacts/0/tmp/circle-
artifacts.DpTK41d/dragonproxy-0.0.3-preR4.jar  
  
RUN wget $JAR_FILE -O /opt/dragonproxy.jar  
  
ADD ./files/supervisord.conf /etc/supervisor/supervisord.conf  
ADD ./files/dragonproxy.conf /etc/supervisor/conf.d/dragonproxy.conf  
ADD ./files/config.yml /opt/config.yml  
  
#EXPOSE 9001  
EXPOSE 19132  
  
WORKDIR /opt  
  
CMD ["/usr/bin/supervisord"]  

