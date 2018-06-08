# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ L __/  
# \ \ __/  
# \\____\\______/  
#  
# -- DOCKERFILE --  
#  
# IHMC UoE NON CAMERA LOGGER  
FROM ubuntu:16.04  
MAINTAINER Doug Stephen <dstephen@ihmc.us>  
  
ENV INITRD No  
ENV LOGGER_VERSION=0.10.0  
ENV IHMC_LOGGER_IP=localhost  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qqy \  
&& DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
  
# Get required base set of tools  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
\  
openjdk-8-jre-headless  
  
RUN mkdir -p /root/.ihmc /root/robotLogs  
  
ADD
https://bintray.com/artifact/download/ihmcrobotics/distributions/IHMCLogger-${LOGGER_VERSION}.tar
/root/IHMCLogger-${LOGGER_VERSION}.tar  
  
RUN tar -xf /root/IHMCLogger-${LOGGER_VERSION}.tar -C /root  
  
RUN rm /root/IHMCLogger-${LOGGER_VERSION}.tar  
  
RUN mv /root/IHMCLogger-${LOGGER_VERSION} /root/IHMCLogger  
  
VOLUME ["/root/robotLogs"]  
  
CMD ["/bin/bash", "-c", "/root/IHMCLogger/bin/IHMCLogger -n -d
/root/robotLogs"]  

