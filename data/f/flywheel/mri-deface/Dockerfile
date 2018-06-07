# flywheel/mri-deface  
#  
# Authorship: Jennifer Reiter  
#  
FROM ubuntu:trusty  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install \  
unzip \  
gzip \  
wget \  
jq  
  
# Make directories for Flywheel v0 Spec  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Download mri_deface nd additional files from MGH  
RUN wget -N -qO- -O ${FLYWHEEL}/mri_deface.gz \  
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/mri_deface-v1.22-Linux64.gz
&& \  
gunzip ${FLYWHEEL}/mri_deface.gz && \  
chmod +x /flywheel/v0/mri_deface  
  
RUN wget -N -qO- -O ${FLYWHEEL}/face.gca.gz \  
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/face.gca.gz && \  
gunzip ${FLYWHEEL}/face.gca.gz  
  
RUN wget -N -qO- -O ${FLYWHEEL}/talairach_mixed_with_skull.gca.gz \  
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/talairach_mixed_with_skull.gca.gz
&& \  
gunzip ${FLYWHEEL}/talairach_mixed_with_skull.gca.gz  
  
ENTRYPOINT ["/flywheel/v0/run"]  

