FROM nexia/ubuntu  
MAINTAINER jgeiger@gmail.com  
  
ENV KAPACITOR_VERSION=kapacitor_1.1.0  
ENV KAPACITOR_FILE=${KAPACITOR_VERSION}_amd64.deb  
  
EXPOSE 9092  
USER root  
  
WORKDIR /tmp  
  
RUN wget --quiet
https://dl.influxdata.com/kapacitor/releases/${KAPACITOR_FILE} \  
&& apt-get -qq -y update \  
&& dpkg -i ${KAPACITOR_FILE} \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
WORKDIR /opt/kapacitor  
  
ENTRYPOINT [ "tini", "--", "/entrypoint.sh"]  
  
CMD [ "kapacitord" ]  

