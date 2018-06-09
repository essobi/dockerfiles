# This Dockerfile constructs a docker image, based on the vistalab/freesurfer-
core  
# docker image, that applies the retinotopic templates from Benson et al.
(2014)  
# PLOS Comput Biol to a FreeSurfer subject.  
#  
# Example build:  
# docker build --no-cache --tag scitran/retinotopy-templates `pwd`  
#  
# Example usage:  
# docker run -v /path/to/your/subject:/input scitran/retinotopy-templates  
#  
# Start with the Freesurfer container  
FROM vistalab/freesurfer  
  
# Note the Maintainer.  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Install system dependencies  
RUN apt-get -y update && apt-get -y install\  
g++ \  
make \  
python \  
python2.7 \  
python-dev \  
python-setuptools \  
python-igraph \  
python-numpy \  
python-scipy \  
libxml2 \  
libxml2-dev \  
zlib1g \  
zlib1g-dev \  
tar \  
zip \  
git \  
gawk \  
tcsh \  
perl-modules \  
libgomp1 \  
bc  
  
# FREESURFER CONFIG  
COPY license /opt/freesurfer/.license  
  
# Download the occipital-atlas-contents  
ENV OCADIR /opt/occipital-atlas/  
WORKDIR ${OCADIR}  
ADD https://storage.googleapis.com/flywheel/gears/data/occipital-
atlas/occipital-atlas-contents.tar.gz /opt/occipital-atlas/  
RUN tar -xf occipital-atlas-contents.tar.gz && \  
rm -f occipital-atlas-contents.tar.gz  
  
# Move relevant files over from contents  
RUN rsync -avP ${OCADIR}/contents/subjects/fsaverage_sym
/opt/freesurfer/subjects/ && \  
rm -rf ${OCADIR}/contents/subjects/fsaverage_sym && \  
rsync -avP ${OCADIR}/contents/subjects/fsaverage /opt/freesurfer/subjects/ &&
\  
rm -rf ${OCADIR}/contents/subjects/fsaverage && \  
mv ${OCADIR}/contents/LICENSE.txt / && \  
mv ${OCADIR}/contents/README.md /  
  
# Copy bin code to container  
COPY bin/apply_template.sh /opt/share/retinotopy-template/apply_template.sh  
COPY bin/run_apply_template.sh /opt/share/retinotopy-
template/run_apply_template.sh  
  
# Make sure the scripts are executable.  
RUN chmod +x /opt/share/retinotopy-template/apply_template.sh  
RUN chmod +x /opt/share/retinotopy-template/run_apply_template.sh  
  
# Install python, and configure neuropythy library  
WORKDIR /opt  
RUN git clone https://github.com/noahbenson/neuropythy  
  
WORKDIR /opt/neuropythy  
RUN python setup.py install && \  
chmod +x /opt/neuropythy/surf2ribbon && \  
ln -s /opt/neuropythy/surf2ribbon /usr/bin/surf2ribbon && \  
ln -s /opt/neuropythy/surf2surf /usr/bin/surf2surf  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
  
# Copy and configure run script and metadata code  
COPY bin/run \  
bin/parse_config.py \  
bin/srf2obj \  
manifest.json \  
${FLYWHEEL}/  
  
# Copy the default config.json file to the container  
COPY bin/config.json ${FLYWHEEL}/default_config.json  
  
# Handle file properties for execution  
RUN chmod +x \  
${FLYWHEEL}/run \  
${FLYWHEEL}/parse_config.py \  
${FLYWHEEL}/srf2obj  
  
# We run the run_apply_template.sh script on entry.  
ENTRYPOINT ["/flywheel/v0/run"]  

