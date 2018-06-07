FROM ubuntu:14.04  
MAINTAINER Milton Pividori <miltondp@gmail.com>  
  
# REQUIREMENTS:  
#  
# EvoMS needs MATLAB R2009 or later. However, this container was tested  
# with MATLAB R2013a.  
#  
# Optional:  
#  
# - Mozilla Firefox® (www.mozilla.com) Version 26 or later, or Google Chrome®  
# (https://www.google.com/intl/en/chrome/browser) Version 30 or later  
# for interactive visualization.  
# - Parallel Computing Toolbox, for multi-core processors or clusters  
# (for parEvoMS_demo and parEvoMS).  
ENV evoms_workdir="/workdir"  
ENV evoms_toolbox_dir="EvoMS-0.2.3-Toolbox"  
RUN mkdir ${evoms_workdir}  
WORKDIR ${evoms_workdir}  
  
# Install base packages  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y \  
wget \  
unzip \  
libxt6 \  
libxmu6 \  
xorg \  
imagemagick && \  
apt-get clean && apt-get autoclean  
  
# Download EvoMS Toolbox  
RUN wget
http://sourceforge.net/projects/sourcesinc/files/evoms/0.2/EvoMS-0.2-Toolbox.zip/download#
\  
-O ./EvoMS-0.2-Toolbox.zip && \  
unzip EvoMS-0.2-Toolbox.zip && \  
rm EvoMS-0.2-Toolbox.zip  
  
COPY run.sh ${evoms_toolbox_dir}/  
RUN chmod -R o+rw ${evoms_toolbox_dir}/  
  
# Download data  
## Example1  
RUN mkdir -p data/Example1 && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1/SETTINGS_Example1.yaml/download#
\  
-O data/Example1/SETTINGS_Example1.yaml && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1/REACTIONS_77.txt/download#
\  
-O data/Example1/REACTIONS_77.txt && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1/COMPOUNDS_Example1.yaml/download#
\  
-O data/Example1/COMPOUNDS_Example1.yaml  
  
## Example2  
RUN mkdir -p data/Example2 && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example2/SETTINGS_Example2.yaml/download#
\  
-O data/Example2/SETTINGS_Example2.yaml && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example2/REACTIONS_154.txt/download#
\  
-O data/Example2/REACTIONS_154.txt && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example2/COMPOUNDS_Example2.yaml/download#
\  
-O data/Example2/COMPOUNDS_Example2.yaml  
  
## Example1r  
RUN mkdir -p data/Example1r && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1r/SETTINGS_Example1r.yaml/download#
\  
-O data/Example1r/SETTINGS_Example1r.yaml && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1r/REACTIONS_77.txt/download#
\  
-O data/Example1r/REACTIONS_77.txt && \  
wget
http://sourceforge.net/projects/sourcesinc/files/evoms/webdata/Example1r/COMPOUNDS_Example1r.yaml/download#
\  
-O data/Example1r/COMPOUNDS_Example1r.yaml  
  
RUN chmod -R o+rw data/  
  
# Create a new user "developer".  
# It will get access to the X11 session in the host computer  
ENV uid=1000  
ENV gid=${uid}  
  
COPY create_user.sh /  
  
# Final steps  
WORKDIR ${evoms_workdir}/${evoms_toolbox_dir}/  
CMD /create_user.sh && sudo -H -u developer /bin/bash  

