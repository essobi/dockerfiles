FROM anishitani/docker-java:oracle-8  
MAINTAINER André Nishitani <andre.nishitani@gmail.com>  
  
ENV GF_MAJOR 4  
ENV GF_MINOR 1  
ENV GF_BUILD 1  
ENV GF_VERSION $GF_MAJOR.$GF_MINOR.$GF_BUILD  
ENV GF_DIR /opt/glassfish$GF_MAJOR  
  
RUN apt-get update -y && apt-get install -y unzip wget \  
&& wget
http://download.java.net/glassfish/$GF_VERSION/release/glassfish-$GF_VERSION.zip
\  
&& unzip -d /opt glassfish-$GF_VERSION.zip \  
&& apt-get purge -y unzip \  
&& apt-get autoclean && apt-get --purge -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* glassfish-$GF_VERSION.zip \  
&& addgroup --system glassfish \  
&& adduser --system --shell /bin/bash --ingroup glassfish glassfish \  
&& chown -R glassfish:glassfish $GF_DIR  
  
ADD ./docker-entrypoint.sh /sbin/docker-entrypoint  
RUN chmod +x /sbin/docker-entrypoint  
  
EXPOSE 80 443 4848 8080 9009  
ENTRYPOINT [ "docker-entrypoint" ]  

