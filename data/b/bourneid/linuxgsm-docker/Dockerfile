#  
# LinuxGSM integrated Dockerfile  
#  
FROM bourneid/linuxgsm-docker-base  
LABEL maintainer="BourneID <admin@h-r-l.co.uk>, on behalf of LinuxGSM"  
  
## user config as LinuxGSM does not run at Root. To help with Volume security,
a known gid and uid will be set to a non-admin user  
RUN groupadd -r lgsm --gid=1337 && useradd -r -g lgsm --uid=1337 lgsm  
  
# Change to the new user and ensure our working directory is set. Note Run is
required due to WORKDIR not being affected by USER  
RUN mkdir /linuxgsm && chown lgsm:lgsm /linuxgsm  
USER lgsm  
WORKDIR /linuxgsm  
  
#Download LinuxGSM and mark as executable  
RUN wget https://linuxgsm.com/dl/linuxgsm.sh && chmod +x linuxgsm.sh  
  
# For checking: Ensure this doesn't override existing data later in the image?  
VOLUME /linuxgsm  
  
# enter a shell.  
CMD /bin/bash  
  

