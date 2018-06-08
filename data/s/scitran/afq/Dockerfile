# Create Docker container that can run afq analysis.  
# Start with the Matlab r2013b runtime container  
FROM vistalab/mcr-v82  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install XVFB and other dependencies  
RUN apt-get update && apt-get install -y xvfb \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
zip \  
unzip \  
python \  
imagemagick \  
wget \  
subversion  
  
# Configure neurodebian repo  
RUN wget -O- http://neuro.debian.net/lists/trusty.us-nh.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80
0xA5D32F012649A5A9  
  
# Install mrtrix and ants  
RUN apt-get update && apt-get install -y \  
mrtrix \  
ants  
  
# Add mrtrix and ants to the system path  
ENV PATH /usr/lib/ants:/usr/lib/mrtrix/bin:$PATH  
  
# ADD the dtiInit Matlab Stand-Alone (MSA) into the container.  
COPY src/bin/AFQ_StandAlone_QMR /usr/local/bin/AFQ  
  
# ADD the control data to the container  
COPY src/data/qmr_control_data.mat /opt/qmr_control_data.mat  
  
# Ensure that the executable files are executable  
RUN chmod +x /usr/local/bin/AFQ  
  
# Handle AFQ and mrD templates via svn mad-hackery  
ENV TEMPLATES /templates  
RUN mkdir $TEMPLATES  
RUN svn export \--force https://github.com/yeatmanlab/AFQ.git/trunk/templates/
$TEMPLATES  
RUN svn export \--force
https://github.com/vistalab/vistasoft.git/trunk/mrDiffusion/templates/
$TEMPLATES  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY run ${FLYWHEEL}/run  
RUN chmod +x ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
ADD
https://raw.githubusercontent.com/scitran/utilities/daf5ebc7dac6dde1941ca2a6588cb6033750e38c/metadata_from_gear_output.py
${FLYWHEEL}/metadata_create.py  
RUN chmod +x ${FLYWHEEL}/metadata_create.py  
COPY src/parse_config.py ${FLYWHEEL}/parse_config.py  
RUN chmod +x ${FLYWHEEL}/parse_config.py  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  
  
# Set the diplay env variable for xvfb  
ENV DISPLAY :1.0  

