# Creates docker container that runs HCP Pipeline algorithms  
#  
#  
# Use Ubuntu 14.04 LTS  
FROM ubuntu:trusty-20170817  
  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Install packages  
RUN apt-get update \  
&& apt-get install -y \  
lsb-core \  
bsdtar \  
zip \  
unzip \  
gzip \  
curl \  
jq \  
python-pip  
  
#############################################  
# Download and install FreeSurfer  
RUN apt-get -y update \  
&& apt-get install -y wget && \  
wget -qO-
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/5.3.0-HCP/freesurfer-
Linux-centos4_x86_64-stable-pub-v5.3.0-HCP.tar.gz | tar zxv -C /opt \  
\--exclude='freesurfer/trctrain' \  
\--exclude='freesurfer/subjects/fsaverage_sym' \  
\--exclude='freesurfer/subjects/fsaverage3' \  
\--exclude='freesurfer/subjects/fsaverage4' \  
\--exclude='freesurfer/subjects/fsaverage5' \  
\--exclude='freesurfer/subjects/fsaverage6' \  
\--exclude='freesurfer/subjects/cvs_avg35' \  
\--exclude='freesurfer/subjects/cvs_avg35_inMNI152' \  
\--exclude='freesurfer/subjects/bert' \  
\--exclude='freesurfer/subjects/V1_average' \  
\--exclude='freesurfer/average/mult-comp-cor' \  
\--exclude='freesurfer/lib/cuda' \  
\--exclude='freesurfer/lib/qt' && \  
apt-get install -y tcsh bc tar libgomp1 perl-modules curl && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Set up the FreeSurfer environment  
ENV OS Linux  
ENV FS_OVERRIDE 0  
ENV FIX_VERTEX_AREA=  
ENV SUBJECTS_DIR /opt/freesurfer/subjects  
ENV FSF_OUTPUT_FORMAT nii.gz  
ENV MNI_DIR /opt/freesurfer/mni  
ENV LOCAL_DIR /opt/freesurfer/local  
ENV FREESURFER_HOME /opt/freesurfer  
ENV FSFAST_HOME /opt/freesurfer/fsfast  
ENV MINC_BIN_DIR /opt/freesurfer/mni/bin  
ENV MINC_LIB_DIR /opt/freesurfer/mni/lib  
ENV MNI_DATAPATH /opt/freesurfer/mni/data  
ENV FMRI_ANALYSIS_DIR /opt/freesurfer/fsfast  
ENV PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5  
ENV MNI_PERL5LIB /opt/freesurfer/mni/lib/perl5/5.8.5  
ENV PATH
/opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
  
#############################################  
# Download and install FSL 5.0.9  
#Build-time key retrieval is sometimes unable to connect to keyserver.
Instead, download the public key manually and store it in plaintext  
#within repo. You should run these commands occassionally to make sure the
saved public key is up to date:  
#gpg --keyserver hkp://pgp.mit.edu:80 --recv 0xA5D32F012649A5A9 && \  
#gpg --export --armor 0xA5D32F012649A5A9 > neurodebian_pgpkey.txt && \  
#gpg --batch --yes --delete-keys 0xA5D32F012649A5A9  
  
COPY neurodebian_pgpkey.txt /tmp/  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl && \  
curl -sSL http://neuro.debian.net/lists/trusty.us-ca.full >>
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key add /tmp/neurodebian_pgpkey.txt && \  
apt-get update && \  
apt-get install -y fsl-core=5.0.9-4~nd14.04+1 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Configure FSL environment  
ENV FSLDIR=/usr/share/fsl/5.0  
ENV FSL_DIR="${FSLDIR}"  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
ENV PATH=/usr/lib/fsl/5.0:$PATH  
ENV FSLMULTIFILEQUIT=TRUE  
ENV POSSUMDIR=/usr/share/fsl/5.0  
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH  
ENV FSLTCLSH=/usr/bin/tclsh  
ENV FSLWISH=/usr/bin/wish  
ENV FSLOUTPUTTYPE=NIFTI_GZ  
  
#############################################  
# Download and install Connectome Workbench  
RUN apt-get update && apt-get -y install connectome-
workbench=1.2.3-1~nd14.04+1  
  
ENV CARET7DIR=/usr/bin  
#############################################  
# Download and install gradient unwarp script  
# note: python-dev needed for Ubuntu 14.04 (but not for 16.04)  
# latest = v1.0.3  
# This commit fixes the memory bug: bab8930e37f1b8ad3a7e274b07c5b3f0f096be85  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends python-dev && \  
apt-get install -y --no-install-recommends python-numpy && \  
apt-get install -y --no-install-recommends python-scipy && \  
apt-get install -y --no-install-recommends python-nibabel && \  
wget -nv https://github.com/Washington-
University/gradunwarp/archive/bab8930e37f1b8ad3a7e274b07c5b3f0f096be85.tar.gz
-O gradunwarp.tar.gz && \  
cd /opt/ && \  
tar zxvf /gradunwarp.tar.gz && \  
mv /opt/gradunwarp-* /opt/gradunwarp && \  
cd /opt/gradunwarp/ && \  
python setup.py install && \  
rm /gradunwarp.tar.gz && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#############################################  
# Download and install HCP Pipelines  
#latest v3.x = v3.22.0  
#latest v4.x = v4.0.0-alpha.5  
#Need to use this 2017-08-24 commit to fix bugs in v4.0.0-alpha.5:
90b0766636ba83f06c9198206cc7fa90117b0b11  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends python-numpy && \  
wget -nv https://github.com/Washington-
University/Pipelines/archive/90b0766636ba83f06c9198206cc7fa90117b0b11.tar.gz
-O pipelines.tar.gz && \  
cd /opt/ && \  
tar zxvf /pipelines.tar.gz && \  
mv /opt/Pipelines-* /opt/HCP-Pipelines && \  
rm /pipelines.tar.gz && \  
cd / && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HCPPIPEDIR=/opt/HCP-Pipelines  
  
#############################################  
# Install MSM binaries (from local directory)  
ENV MSMBin=${HCPPIPEDIR}/MSMBinaries  
  
# Copy MSM_HOCR_v2 binary  
# Skip this for now pending license questions  
#COPY MSM/Centos/msm ${MSMBin}/msm  
#############################################  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
WORKDIR ${FLYWHEEL}  
  
# Copy executable/manifest to Gear  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Copy additional scripts and scenes  
COPY scripts/*.sh scripts/*.bat ${FLYWHEEL}/scripts/  
  
# ENV preservation for Flywheel Engine  
RUN env -u HOSTNAME -u PWD | \  
awk -F = '{ print "export " $1 "=\"" $2 "\"" }' > ${FLYWHEEL}/docker-env.sh  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  

