# This Dockerfile constructs a docker image, based on the vistalab/freesurfer  
# docker image to execute recon-all as a Flywheel Gear.  
#  
# Example build:  
# docker build --no-cache --tag scitran/freesurfer-recon-all `pwd`  
#  
# Example usage:  
# docker run -v /path/to/your/subject:/input scitran/freesurfer-recon-all  
#  
FROM ubuntu:trusty  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install dependencies for FreeSurfer  
RUN apt-get update && apt-get -y install \  
bc \  
tar \  
zip \  
wget \  
gawk \  
tcsh \  
python \  
libgomp1 \  
python2.7 \  
perl-modules  
  
# Download Freesurfer v6.0.0 from MGH and untar to /opt  
RUN wget -N -qO-
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-
centos6_x86_64-stable-pub-v6.0.0.tar.gz | tar -xz -C /opt && chown -R
root:root /opt/freesurfer  
  
# The brainstem and hippocampal subfield modules in FreeSurfer 6.0 require the
Matlab R2012 runtime  
RUN apt-get install -y libxt-dev libxmu-dev  
ENV FREESURFER_HOME /opt/freesurfer  
RUN wget -N -qO-
"http://surfer.nmr.mgh.harvard.edu/fswiki/MatlabRuntime?action=AttachFile&do=get&target=runtime2012bLinux.tar.gz"
| tar -xz -C $FREESURFER_HOME && chown -R root:root /opt/freesurfer/MCRv80  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY bin/run \  
bin/parse_config.py \  
bin/srf2obj \  
manifest.json \  
${FLYWHEEL}/  
  
# Handle file properties for execution  
RUN chmod +x \  
${FLYWHEEL}/run \  
${FLYWHEEL}/srf2obj \  
${FLYWHEEL}/parse_config.py  
  
# Run the run.sh script on entry.  
ENTRYPOINT ["/flywheel/v0/run"]  

