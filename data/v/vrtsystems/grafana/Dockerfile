# vim:set ft=dockerfile:  
# Base on VRT Base image  
FROM vrtsystems/baseimage:0.2.0  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# add our user and group first to make sure their IDs get assigned  
# consistently, regardless of whatever dependencies get added later  
RUN groupadd -r grafana && useradd -r -g grafana grafana  
  
ENV GRAFANA_VERSION 4.5.2  
ENV GF_PRESTART_INIT_D=/usr/local/etc/docker-grafana/prestart-init.d  
ENV GF_POSTSTART_INIT_D=/usr/local/etc/docker-grafana/poststart-init.d  
  
RUN curl https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana_${GRAFANA_VERSION}_amd64.deb > /tmp/grafana_amd64.deb
\  
&& apt-get update && apt-get -y install libfontconfig adduser openssl ca-
certificates \  
&& dpkg -i /tmp/grafana_amd64.deb \  
&& echo "=== Add prestart-init.d ===============" \  
&& mkdir -p ${GF_PRESTART_INIT_D} \  
&& echo "=== Add poststart-init.d ===============" \  
&& mkdir -p ${GF_POSTSTART_INIT_D} \  
&& mkdir -p /var/local/grafana \  
&& chown -R grafana:grafana /var/local/grafana \  
&& echo "=== Cleaning up ========================" \  
&& rm /tmp/grafana_amd64.deb \  
&& /usr/local/sbin/docker-cleanup.sh  
  
# The following updates Grafana's defaults.ini file to set default  
# paths for data and logs. Note that this should be achievable  
# via changes to grafana.ini or via environment variables, but for  
# issue 2533 (https://github.com/grafana/grafana/issues/2533) which  
# despite being closed before release of 2.1.2, doesn't seem to  
# have fixed the issue  
RUN echo "=== Tweaking Defaults ========================" \  
&& ls -l /etc/grafana/grafana.ini /usr/share/grafana/conf/defaults.ini \  
&& sed -i 's/\;mode = console\, file/mode = console/' /etc/grafana/grafana.ini
\  
&& sed -i 's/mode = console\, file/mode = console/'
/usr/share/grafana/conf/defaults.ini \  
&& sed -i 's/data = \/var\/lib\/grafana/data = \/var\/local\/grafana/'
/etc/grafana/grafana.ini \  
&& sed -i 's/data = data/data = \/var\/local\/grafana/'
/usr/share/grafana/conf/defaults.ini \  
&& sed -i 's/logs = \/var\/log\/grafana/logs = \/var\/local\/grafana\/logs/'
/etc/grafana/grafana.ini \  
&& sed -i 's/logs = data\/log/logs = \/var\/local\/grafana\/logs/'
/usr/share/grafana/conf/defaults.ini  
  
COPY docker-entrypoint.sh /usr/local/sbin/  
COPY supervisord-postinit.sh /usr/local/sbin/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 3000  
VOLUME ["/var/local/"]  
  
WORKDIR ["/usr/share/grafana"]  
  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
  
CMD ["supervisor"]  

