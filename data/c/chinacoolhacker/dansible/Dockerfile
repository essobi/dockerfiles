FROM centos:7  
RUN yum -y install epel-release.noarch centos-release-openshift-origin.noarch
\  
&& yum -y install python-pip \  
&& yum -y update \  
&& pip install --upgrade pip \  
&& yum -y install gcc make pyOpenSSL python-devel openssl openssl-devel bind-
utils git httpd-tools vim strace origin-clients python2-jmespath \  
&& pip install ansible python-openstackclient python-neutronclient python-
novaclient python-heatclient python-cinderclient setuptools boto --upgrade \  
&& pip install pyzabbix influxdb urllib3 six requests python_dateutil idna
chardet certifi \  
&& useradd -m -d /scripts -s /bin/bash jenkins  
  
USER jenkins  
ENV HOME /scripts  
VOLUME [ /scripts ]  
WORKDIR /scripts  
  
CMD [ '/bin/bash' ]  
  

