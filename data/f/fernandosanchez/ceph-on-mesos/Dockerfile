FROM java:8-jre  
ARG http_proxy  
ENV http_proxy ${http_proxy}  
ENV VERSION ceph-on-mesos-0.2.11  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv E56151BF \  
&& echo "deb http://repos.mesosphere.com/debian jessie-unstable main" | tee
/etc/apt/sources.list.d/mesosphere.list \  
&& echo "deb http://repos.mesosphere.com/debian jessie-testing main" | tee -a
/etc/apt/sources.list.d/mesosphere.list \  
&& echo "deb http://repos.mesosphere.com/debian jessie main" | tee -a
/etc/apt/sources.list.d/mesosphere.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \--force-yes
mesos=1.0.1-2.0.93.debian81 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/mnt/mesos/sandbox/${VERSION}/bin/ceph-on-mesos --api-
port=$PORT0"]  

