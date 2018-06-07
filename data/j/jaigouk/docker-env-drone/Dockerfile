# docker-env-drone v0.1  
FROM phusion/baseimage  
MAINTAINER "Jaigouk Kim" <ping@jaigouk.kim>  
  
RUN echo "update system and install needed deps" \  
&& apt-get update -y -qq \  
&& apt-get install -y -qq wget libsqlite3-dev \  
&& echo "install drone" \  
&& cd /tmp \  
&& wget http://downloads.drone.io/master/drone.deb \  
&& dpkg -i drone.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 8282  
ENTRYPOINT ["/usr/local/bin/droned"]  
CMD ["--config=/data/droneio/drone_conf.toml"]  

