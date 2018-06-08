FROM debian:jessie  
  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
ENV MONIT_VERSION 5.25.1  
RUN apt-get update \  
&& apt-get install --yes wget build-essential libz-dev libpam0g-dev libssl-dev
lm-sensors net-tools libltdl-dev links \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -qO- https://mmonit.com/monit/dist/monit-"$MONIT_VERSION".tar.gz |
tar -xvz -C /tmp  
  
RUN cd /tmp/monit-"$MONIT_VERSION" \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rfv monit-"$MONIT_VERSION"  
  
RUN mkdir -v /usr/local/etc/monitrc \  
&& chmod -v 700 /usr/local/etc/monitrc  
  
COPY ./monitrc /usr/local/etc/monitrc  
RUN chmod -v 700 /usr/local/etc/monitrc/monitrc  
RUN chmod -v 755 /usr/local/etc/monitrc/script.d/*.sh  
  
RUN mkdir -v /docker-entrypoint.d  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod -v 755 /docker-entrypoint.sh  
  
EXPOSE 2812  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/local/bin/monit", "-I", "-c", "/usr/local/etc/monitrc/monitrc"]  

