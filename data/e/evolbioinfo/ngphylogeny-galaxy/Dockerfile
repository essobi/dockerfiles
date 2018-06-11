# Modified galaxy with environment modules and singularity  
# https://hub.docker.com/r/bgruening/galaxy-stable/  
# latest  
# base image: galaxy-stable  
FROM bgruening/galaxy-stable:18.01  
# File Author / Maintainer  
MAINTAINER Frederic Lemoine <frederic.lemoine@pasteur.fr>  
  
ENV MODULE_PACKAGES="/packages"  
ENV
GALAXY_CONFIG_TOOL_CONFIG_FILE=config/tool_conf.xml.sample,config/shed_tool_conf.xml.sample,/local_tools/tool_conf.xml  
ENV GALAXY_DOCKER_ENABLED=True  
  
## Install environment modules & singularity  
RUN apt-get update --fix-missing \  
&& apt-get install -y wget libssl-dev libssl1.0.0 \  
&& sudo apt-get update \  
&& apt-get install -y environment-modules squashfs-tools libtool libarchive-
dev \  
&& git clone https://github.com/singularityware/singularity.git \  
&& cd singularity \  
&& git checkout 2.5.0 \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf singularity \  
&& apt-get remove -y libssl-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Copy docker init files  
COPY docker/init_modules.sh $GALAXY_HOME/docker/  
COPY docker/package_list.txt $GALAXY_HOME/docker/  
  
## Installs singularity images and their  
## available commands into module paths  
RUN mkdir /packages \  
&& cd $GALAXY_HOME/docker/ \  
&& ./init_modules.sh  
  
## Auto initialize environment modules for bash and sh  
RUN echo "source /usr/share/modules/init/bash" >> /etc/bash.bashrc  
RUN echo "source /usr/share/modules/init/sh" >> /etc/profile  
  
## COPY Galaxy conf files into right directories  
COPY docker/dependency_resolvers_conf.xml /galaxy-
central/config/dependency_resolvers_conf.xml  
COPY docker/environment_modules_mapping.yml /galaxy-
central/config/environment_modules_mapping.yml  
## COPY tool wrappers  
COPY tools /local_tools/  
## COPY workflows  
COPY workflows/* $GALAXY_HOME/workflows/  
  
# We make galaxy folders available to singularity runs  
RUN echo "bind path = /export:/export" >>
/usr/local/etc/singularity/singularity.conf \  
&& echo "bind path = /data:/data" >>
/usr/local/etc/singularity/singularity.conf  
  
# We import workflows  
RUN startup_lite && \  
galaxy-wait && \  
workflow-install --workflow_path $GALAXY_HOME/workflows/ -g
http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p
$GALAXY_DEFAULT_ADMIN_PASSWORD  
  
RUN mv /galaxy-central/config/datatypes_conf.xml.sample /galaxy-
central/config/datatypes_conf.xml  
  

