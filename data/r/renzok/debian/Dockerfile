#  
# Just a simple image already defining some layers  
# * a common single non-root user called mate  
# * curl as download tool  
# * en_US UTF locale  
#  
FROM debian:jessie  
  
MAINTAINER Renzo Kottmann <renzo.kottmann@gmail.com>  
  
# Got this from Turnbull "The Docker Book"  
# declare a variable and change if you want to trigger new build of  
# layers (could also be done with --no-cache) but this has the  
# adavantage of documenting when last modified :) )  
ENV LAST_DOCKER_IMAGE_BUILD='2017-02-12'  
ENV USER=mate USER_ID=1000 \  
HOST_GROUP=boatswain HOST_GID=7777  
# perform setgid in mkdir and chmod in case future docker versions  
# support it  
RUN groupadd --gid "${HOST_GID}" "${HOST_GROUP}" && \  
useradd --create-home --shell /bin/bash \  
\--uid ${USER_ID} \--groups ${HOST_GROUP} ${USER}  
  
RUN apt-get update -qq && \  
apt-get install --auto-remove -qq -y \  
locales \  
less \  
curl && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
localedef -i en_US -c -f UTF-8 \  
-A /usr/share/locale/locale.alias en_US.UTF-8  
  
ENTRYPOINT ["/bin/true"]  

