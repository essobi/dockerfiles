# Dockerizing HTCondor submit node  
# Based on debian:wheezy, installs HTCondor following the instructions from:  
# https://research.cs.wisc.edu/htcondor/debian/  
  
FROM ubuntu:14.04  
MAINTAINER Riccardo Bucchi <riccardo.bucchi26@gmail.com>  
ENV TINI_VERSION v0.9.0  
EXPOSE 5000  
EXPOSE 22  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
RUN set -ex \  
# CONDOR  
&& apt-get update && apt-get install -y wget procps curl \  
&& chmod +x /sbin/tini \  
&& echo "deb http://research.cs.wisc.edu/htcondor/ubuntu/stable/ trusty
contrib" >> /etc/apt/sources.list \  
&& wget -qO - http://research.cs.wisc.edu/htcondor/ubuntu/HTCondor-
Release.gpg.key | apt-key add \- \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install condor -y \--force-yes \  
&& apt-get install -y python-pip && pip install supervisor supervisor-stdout \  
# ONECLIENT  
&& apt-get install fuse -y \  
&& wget --no-check-certificate -q https://get.onedata.org/oneclient.sh \  
&& chmod 775 oneclient.sh \  
&& ./oneclient.sh \  
&& mkdir /var/log/oneclient \  
# HEALTHCHECKS  
&& mkdir -p /opt/health/master/ /opt/health/executor/ /opt/health/submitter/ \  
&& apt-get install -y python-pip && pip install Flask \  
# SSHD  
&& apt-get install -y openssh-server && mkdir -p /var/log/ssh/ && mkdir
/var/run/sshd && mkdir /root/.ssh \  
# CLEAN  
&& apt-get -y remove python-pip \  
&& apt-get clean all  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY condor_config /etc/condor/condor_config  
COPY master_healthcheck.py /opt/health/master/healthcheck.py  
COPY executor_healthcheck.py /opt/health/executor/healthcheck.py  
COPY submitter_healthcheck.py /opt/health/submitter/healthcheck.py  
COPY sshd_config /etc/ssh/sshd_config  
COPY run.sh /usr/local/sbin/run.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/run.sh"]  

