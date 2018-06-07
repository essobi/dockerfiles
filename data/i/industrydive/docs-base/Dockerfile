FROM debian:wheezy  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
netcat \  
curl \  
python-pip \  
python-dev \  
libmysqlclient-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
build-essential \  
python-sphinx \  
libpq-dev \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
# Install airflow and its dependencies.  
RUN pip install cryptography \  
&& pip install airflow==1.5.1 \  
&& pip install airflow[mysql]==1.5.1 \  
&& pip install sphinx-rtd-theme==0.1.9  
# Base command runs make on working dir's make file.  
# Docs container must expose its Makefile at its working dir.  
CMD ["make", "html"]  

