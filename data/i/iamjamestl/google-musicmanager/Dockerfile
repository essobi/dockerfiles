#  
# Google Music Manager Dockerfile  
# Copyright (C) 2017 James T. Lee  
#  
# Google Music Manager works on Debian, Ubuntu, Fedora, and OpenSuSE. Choose  
# Ubuntu because it has good LTS images and, as the most popular Linux
desktop,  
# Music Manager is more likely to run best on it.  
FROM ubuntu  
  
# Download and install the google-musicmanager package directly, with  
# dependencies. This is done as opposed to configuring the Google apt  
# repositories and getting it through the package manager, which is not  
# documented and seems to suffer from some invalid metadata issues.  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget https://dl.google.com/linux/direct/google-musicmanager-
beta_current_amd64.deb \  
&& apt install -y ./google-musicmanager-beta_current_amd64.deb \  
&& rm -f google-musicmanager-beta_current_amd64.deb \  
&& apt-get remove --purge --auto-remove -y wget \  
&& rm -rf /var/cache/apt/lists/*  
  
# Set up links so the program can find its config and default music source  
# out-of-the-box while being user-friendly from the docker side. These are not  
# explicitly exposed as "volumes" so that Docker doesn't create empty  
# directories for them. I'd rather Music Manager fail than to write its config  
# to a directory that the user forgot to map in to the container.  
RUN mkdir -p /root/.config \  
&& ln -sf /config /root/.config/google-musicmanager \  
&& ln -sf /music /root/Music  
  
# The google-musicmanager process daemonizes itself with no option to run in
in  
# the foreground, so wrap it to wait for the daemon process to exit, and pass
a  
# couple signals around.  
COPY google-musicmanager-wrapper /  
  
# Run google-musicmanager with the wrapper and have it find our music volume.  
CMD ["/google-musicmanager-wrapper", "-s", "/music"]  

