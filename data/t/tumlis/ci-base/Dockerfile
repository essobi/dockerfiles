FROM ubuntu:16.04  
LABEL maintainer="Philipp Wagner <philipp.wagner@tum.de>"  
LABEL description="Base image for CI builds at TUM LIS with GitLab Runner"  
  
# Install common dependencies, including EDA-tool specific dependencies  
# and build tools to avoid fetching them again for every build.  
#  
# Tested tools:  
# - Xilinx Vivado 2017.4  
# - Synopsys VCS M-2017.3  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y git-core libtcl8.5 curl gosu sudo \  
build-essential automake autoconf pkg-config tcl \  
python python-pip \  
python3 python3-dev python3.5-venv python3-pip libffi-dev \  
dc fontconfig libaudio2 libc6 libfontconfig1 libfreetype6 libgcc1 \  
libglib2.0-0 libice6 libjpeg8 libmng2 libpng12-0 libsm6 libstdc++6 \  
libtiff5 libx11-6 libxext6 libxi6 libxrender1 zlib1g libxrandr2 \  
&& rm -rf /var/lib/apt/lists/*  
  
# use bash as default shell  
RUN ln -sf /bin/bash /bin/sh  
  
# add service account user (UID/GID to be replaced)  
RUN groupadd sa \  
&& useradd --create-home -g sa sa \  
&& usermod -p '*' sa \  
&& passwd -u sa  
  
COPY start.sh /start.sh  
COPY sudoconf /etc/sudoers.d/sa  
COPY env_modules /bashenv.sh  
  
ENTRYPOINT [ "/start.sh" ]  

