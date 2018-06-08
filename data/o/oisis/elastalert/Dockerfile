FROM python:2  
MAINTAINER OiSiS (https://github.com/oisis)  
  
ENV ELASTALERT_VERSION v0.0.95  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
# Switch to bash  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
RUN apt-get update \  
&& apt-get -yqq install \  
wget \  
unzip \  
python-pip \  
virtualenv \  
python-dev \  
&& pip install envtpl  
  
RUN wget "https://github.com/Yelp/elastalert/archive/v0.0.95.zip" -O
/root/elastalert-v0.0.95.zip \  
&& unzip /root/elastalert-v0.0.95.zip -d /root \  
&& rm -f /root/elastalert-v0.0.95.zip \  
&& mv /root/elastalert-0.0.95 /root/elastalert \  
&& rm -rf /root/elastalert/docs \  
/root/elastalert/example_rules \  
/root/elastalert/config.yaml.example \  
&& mkdir /root/elastalert/rules \  
&& cd /root/elastalert/ \  
&& virtualenv virtualenvelastalert \  
&& source virtualenvelastalert/bin/activate \  
&& python setup.py install  
  
COPY configs/config.yaml.tpl /root/elastalert/  
COPY scripts/run_elastalert.sh /run_elastalert.sh  
COPY rules/ /root/elastalert/rules  
RUN chmod +x /run_elastalert.sh  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
# Volumes to mount:  
VOLUME ['/root/elastalert/rules/']  
  
ENTRYPOINT ["/run_elastalert.sh"]  

