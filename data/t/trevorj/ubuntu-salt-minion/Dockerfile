ARG SALTY_PARENT_IMAGE="trevorj/boilerplate"  
ARG SALTY_PARENT_TAG="latest"  
FROM $SALTY_PARENT_IMAGE:$SALTY_PARENT_TAG  
  
MAINTAINER Trevor Joynson "<docker@trevor.joynson.io>"  
# Latest  
ARG SALTY_RELEASE="latest"  
ARG SALTY_PACKAGES="salt-minion salt-master salt-api salt-cloud salt-ssh nacl-
tools git"  
## Pinned  
#ARG SALTY_RELEASE="2016.3"  
# Lazy automagic (eval'd later, don't judge me)  
ARG SALTY_APT_RELEASE="\${DISTRIB_RELEASE}/\${DISTRIB_ARCH}/\${SALTY_RELEASE}"  
# Build repo URL  
ARG
SALTY_APT_REPO="http://repo.saltstack.com/apt/ubuntu/\${SALTY_APT_RELEASE}"  
# Install salt-minion  
COPY build.d $IMAGE_ROOT/build.d  
RUN build-parts "$IMAGE_ROOT/build.d"  
  
# Add in files  
ADD image $IMAGE_ROOT/  
  
VOLUME ["/etc/salt/pki", "/srv/salt", "/srv/pillar"]  
EXPOSE 4505 4506  
# Fucking CI docker is from 1999.  
#HEALTHCHECK --interval=5m --timeout=3s CMD-SHELL nc -z localhost 4505 && nc
-z localhost 4506 || exit 1  

