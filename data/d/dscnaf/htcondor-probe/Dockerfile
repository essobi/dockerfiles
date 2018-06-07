# Dockerizing HTCondor probe  
# Based on ubuntu:14.04  
# using https://github.com/fifemon/probes  
  
FROM ubuntu:14.04  
MAINTAINER Riccardo Bucchi <riccardo.bucchi26@gmail.com>  
ENV TINI_VERSION v0.9.0  
EXPOSE 5000  
EXPOSE 22  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
RUN set -ex \  
&& apt-get update && apt-get install -y wget git procps \  
&& chmod +x /sbin/tini \  
# unfortunately htcondor is required for classad python libraries  
&& echo "deb http://research.cs.wisc.edu/htcondor/ubuntu/stable/ trusty
contrib" >> /etc/apt/sources.list \  
&& wget -qO - http://research.cs.wisc.edu/htcondor/ubuntu/HTCondor-
Release.gpg.key | apt-key add \- \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install condor -y \--force-yes \  
&& apt-get install -y python-pip && pip install virtualenv supervisor
supervisor-stdout \  
# MONITOR  
&& git clone https://github.com/fifemon/probes /opt/probes \  
&& virtualenv --system-site-packages /opt/probes/venv && /bin/bash -c "source
/opt/probes/venv/bin/activate" && pip install supervisor influxdb \  
# CLEAN  
&& apt-get -y remove python-pip git \  
&& apt-get clean all  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY run.sh /usr/local/sbin/run.sh  
COPY condor-probe.cfg /opt/probes/etc/condor-probe.cfg  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/run.sh"]  

