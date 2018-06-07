FROM aggurio/dey-base:latest  
  
MAINTAINER Alex Gonzalez <alex.gonzalez@digi.com>  
  
ENV HOME="/home/dey"  
# Create project  
RUN mkdir -p ${HOME}/workspace/ccimx6sbc && cd ${HOME}/workspace/ccimx6sbc &&
source /usr/local/dey-2.0/mkproject.sh -p ccimx6sbc <<< "y"  
  
WORKDIR ${HOME}/workspace/ccimx6sbc  
  
# Configure local.conf file  
RUN echo 'INHERIT += "rm_work"' >> ${HOME}/workspace/ccimx6sbc/conf/local.conf
&& echo 'DISTRO_FEATURES_remove = "x11"' >>
${HOME}/workspace/ccimx6sbc/conf/local.conf  
  
# Build default image  
RUN source ${HOME}/workspace/ccimx6sbc/dey-setup-environment && bitbake dey-
image-qt && rm -Rf downloads tmp  
  

