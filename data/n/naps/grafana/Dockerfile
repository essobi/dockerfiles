FROM debian:stretch  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV GRAFANA_VERSION 4.6.3  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install adduser libfontconfig \  
&& apt-get clean  
  
ADD https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana_${GRAFANA_VERSION}_amd64.deb /tmp/grafana.deb  
RUN dpkg -i /tmp/grafana.deb  
  
RUN mkdir /grafana && mkdir /grafana/data  
  
ADD default_grafana.ini /grafana/grafana.ini  
  
RUN addgroup --quiet --system grafana  
RUN adduser --home /grafana --group --quiet --system grafana  
  
RUN chown grafana:grafana -R /grafana && chmod 755 -R /grafana  
  
USER grafana:grafana  
  
EXPOSE 3000  
VOLUME /var/logs  
VOLUME /grafana  
  
CMD []  
WORKDIR /usr/share/grafana/  
ENTRYPOINT ["/usr/sbin/grafana-server", "-config=/grafana/grafana.ini",
"cfg:default.paths.logs=/grafana/data/",
"cfg:default.paths.data=/grafana/logs/"]  

