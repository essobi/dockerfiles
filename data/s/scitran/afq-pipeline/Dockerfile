# Create Docker container that can run afq analysis.  
# Start with the Matlab r2013b runtime container  
FROM flywheel/matlab-mcr:v82  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
ENV FLYWHEEL /flywheel/v0  
WORKDIR ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
  
###########################  
# Install dependencies  
# Configure neurodebian  
# (https://github.com/neurodebian/dockerfiles/blob/master/dockerfiles/trusty-
non-free/Dockerfile)  
RUN set -x \  
&& apt-get update \  
&& { \  
which gpg \  
|| apt-get install -y --no-install-recommends gnupg \  
; } \  
# Ubuntu includes "gnupg" (not "gnupg2", but still 2.x), but not dirmngr, and
gnupg 2.x requires dirmngr  
# so, if we're not running gnupg 1.x, explicitly install dirmngr too  
&& { \  
gpg --version | grep -q '^gpg (GnuPG) 1\\.' \  
|| apt-get install -y --no-install-recommends dirmngr \  
; } \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
DD95CC430502E37EF840ACEEA5D32F012649A5A9 \  
&& gpg --export DD95CC430502E37EF840ACEEA5D32F012649A5A9 >
/etc/apt/trusted.gpg.d/neurodebian.gpg \  
&& rm -rf "$GNUPGHOME" \  
&& apt-key list | grep neurodebian  
  
RUN { \  
echo 'deb http://neuro.debian.net/debian trusty main'; \  
echo 'deb http://neuro.debian.net/debian data main'; \  
} > /etc/apt/sources.list.d/neurodebian.sources.list  
  
RUN sed -i -e 's,main *$,main contrib non-free,g'
/etc/apt/sources.list.d/neurodebian.sources.list; grep -q 'deb .* multiverse$'
/etc/apt/sources.list || sed -i -e 's,universe *$,universe multiverse,g'
/etc/apt/sources.list  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y --force-yes \  
xvfb \  
xfonts-100dpi \  
xfonts-75dpi \  
xfonts-cyrillic \  
zip \  
unzip \  
python \  
imagemagick \  
wget \  
subversion \  
fsl-5.0-core \  
jq \  
mrtrix \  
ants  
  
############################  
# AFQ  
# Add mrtrix and ants to the system path  
ENV PATH /usr/lib/ants:/usr/lib/mrtrix/bin:$PATH  
  
# ADD the source Code and Binary to the container  
COPY afq/source/bin/AFQ_StandAlone_QMR /usr/local/bin/AFQ  
COPY afq/run ${FLYWHEEL}/run_afq  
COPY afq/source/parse_config.py ${FLYWHEEL}/afq_parse_config.py  
RUN chmod +x /usr/local/bin/AFQ ${FLYWHEEL}/afq_parse_config.py  
  
# ADD the control data to the container  
COPY afq/source/data/qmr_control_data.mat /opt/qmr_control_data.mat  
  
# ADD AFQ and mrD templates via svn hackery  
ENV TEMPLATES /templates  
RUN mkdir $TEMPLATES  
RUN svn export \--force https://github.com/yeatmanlab/AFQ.git/trunk/templates/
$TEMPLATES  
RUN svn export \--force
https://github.com/vistalab/vistasoft.git/trunk/mrDiffusion/templates/
$TEMPLATES  
  
# Set the diplay env variable for xvfb  
ENV DISPLAY :1.0  
############################  
# DTIINIT  
# ADD the dtiInit Matlab Stand-Alone (MSA) into the container.  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/dtiInit/standalone/executables/dtiInit_glnxa64_v82
/usr/local/bin/dtiInit  
  
# Add bet2 (FSL) to the container  
ADD https://github.com/vistalab/vistasoft/raw/97aa8a8/mrAnatomy/Segment/bet2
/usr/local/bin/  
  
# Add the MNI_EPI template and JSON schema files to the container  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/templates/MNI_EPI.nii.gz
/templates/  
ADD
https://github.com/vistalab/vistasoft/raw/97aa8a8/mrDiffusion/dtiInit/standalone/dtiInitStandAloneJsonSchema.json
/templates/  
  
# Copy the help text to display when no args are passed in.  
COPY dtiinit/source/doc/help.txt /opt/help.txt  
  
# Ensure that the executable files are executable  
RUN chmod +x /usr/local/bin/bet2 /usr/local/bin/dtiInit  
  
# Configure environment variables for bet2  
ENV FSLOUTPUTTYPE NIFTI_GZ  
  
# Copy and configure code  
WORKDIR ${FLYWHEEL}  
COPY dtiinit/source/bin/run ${FLYWHEEL}/run_dtiinit  
COPY dtiinit/source/bin/parse_config.py ${FLYWHEEL}/dtiinit_parse_config.py  
  
######################  
# FSLMERGE  
COPY fslmerge/source/run ${FLYWHEEL}/run_fslmerge  
  
############################  
# Configure entrypoint  
RUN chmod +x ${FLYWHEEL}/*  
ENTRYPOINT ["/flywheel/v0/run"]  
COPY manifest.json ${FLYWHEEL}/manifest.json  

