FROM prom/prometheus:0.16.1  
RUN apk \--update add openssl \  
&& apk -t deps \--update \--repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ add runit \  
&& wget -O -
https://github.com/prometheus/alertmanager/releases/download/0.0.3/alertmanager-0.0.3.linux-
amd64.tar.gz \  
| tar -C /bin/ -xzf - \  
&& wget -O - https://github.com/docker-
infra/reefer/releases/download/v0.0.4/reefer.gz | zcat > /bin/reefer \  
&& wget -O -
https://github.com/mesosphere/mesos_exporter/releases/download/v1.0-rc1/mesos-
exporter-v1.0-rc1-amd64-linux.gz | zcat > /bin/mesos-exporter \  
&& wget -O -
https://github.com/discordianfish/zookeeper_exporter/releases/download/0.0.1/zookeeper_exporter-v0.0.1-amd64-linux.gz
| zcat > /bin/zookeeper_exporter \  
&& chmod a+x /bin/reefer /bin/mesos-exporter /bin/zookeeper_exporter \  
&& apk del openssl  
ADD . /etc  
RUN promtool check-rules /etc/prometheus/prometheus.rules  
EXPOSE 9090 9093  
ENTRYPOINT [ "/bin/reefer", \  
"-t", "/etc/prometheus/alertmanager.conf.tmpl", \  
"/sbin/runsvdir", "/etc/service" ]  

