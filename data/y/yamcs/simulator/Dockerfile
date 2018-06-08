FROM openjdk:8-jdk  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# enable utf-8 enabled by default  
RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends maven \  
&& env GIT_SSL_NO_VERIFY=true git clone \--depth 1 --branch yamcs-3.1.0
https://github.com/yamcs/yamcs.git \  
&& cd yamcs \  
&& mvn package -DskipTests \  
&& mkdir /opt/yamcs \  
&& ./make-live-devel.sh /opt/yamcs \  
&& rm -rf .git \  
&& rm -rf ~/.m2 \  
&& apt-get purge -y --auto-remove maven \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt/yamcs  
  
COPY simulator.yaml /opt/yamcs/etc/simulator.yaml  
  
# TM & TC  
EXPOSE 10015 10025  
CMD ["bin/simulator.sh"]  

