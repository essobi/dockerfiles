# Pulsar Docker Image  
# Run a Pulsar Server on a Docker Container  
# Version 1.0.0  
FROM ubuntu:14.04  
MAINTAINER Alexandre Defelicibus, adefelicibus@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
RUN apt-get -qq update && \  
apt-get install --no-install-recommends -y software-properties-common && \  
apt-get -qq update && \  
apt-get install --no-install-recommends -y build-essential libgd2-xpm-dev \  
python-dev python-virtualenv \  
libswitch-perl libcurl4-openssl-dev python-pip \  
python2.7 python2.7-dev git default-jre \  
libffi-dev libssl-dev && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
RUN mkdir /usr/share/pulsar; chmod 755 /usr/share/pulsar  
RUN virtualenv /usr/share/pulsar/venv  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
pyOpenSSL  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
PasteDeploy  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
paste  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
numpy  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed bx-
python mako  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
pycurl  
  
RUN . /usr/share/pulsar/venv/bin/activate; pip install --ignore-installed
pulsar-app==0.7.2  
  
RUN . /usr/share/pulsar/venv/bin/activate; cd /usr/share/pulsar; pulsar-config  
  
# Install needed modules  
RUN cpan App::cpanminus  
RUN cpanm URI::Escape  
RUN cpanm GD::Graph::bars  
RUN cpanm PerlIO::gzip  
  
ADD env_container.sh /usr/share/pulsar/env_container.sh  
ADD startup.sh /usr/sbin/startup.sh  
ADD app.yml /usr/share/pulsar/  
ADD server.ini /usr/share/pulsar/  
ADD local_env.sh /usr/share/pulsar/  
  
RUN ln -s /mnt/shed_tools/ /shed_tools  
RUN ln -s /mnt/ /galaxy-central  
RUN ln -s /mnt/tool_deps /tool_deps  
RUN ln -s
/mnt/shed_tools/toolshed.g2.bx.psu.edu/repos/peterjc/mira4_assembler/a4f602cc3aa9/mira4_assembler/tools/mira4_0/mira4_make_bam.py
/usr/share/pulsar/venv/lib/python2.7/site-packages/  
  
RUN chmod +x /usr/sbin/startup.sh  
RUN chmod +x /usr/share/pulsar/env_container.sh  
  
EXPOSE :8913  
# VOLUME ["/pulsar"]  
ENTRYPOINT ["/usr/sbin/startup.sh"]

