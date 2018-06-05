# This Dockerfile is based on the dockerfile 'fmriprep' from the Poldrack  
# Lab (https://github.com/poldracklab/fmriprep) and 'nipype_env' from Michael
Notter (https://github.com/miykael/nipype_env). The jupyter notebook
foundation  
# is based on jupyter/docker-stacks's jupyter/datascience-notebook.  
#  
# This means that the same copyrights apply to this Dockerfile, as they do for  
# the above mentioned dockerfiles.  
FROM jupyter/datascience-notebook  
MAINTAINER Till Schellhorn <tschellhorn@gmail.com>  
  
#---------------------------------------------  
# Update OS dependencies and setup neurodebian  
#---------------------------------------------  
USER root  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends bzip2 \  
ca-certificates \  
curl \  
git \  
tree \  
unzip \  
wget \  
xvfb \  
zip  
ENV NEURODEBIAN_URL http://neuro.debian.net/lists/jessie.de-md.full  
RUN curl -sSL $NEURODEBIAN_URL | sudo tee
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 &&
\  
apt-get update -qq  
  
#----------------------------------------------------  
# Update and install conda dependencies for python2.7  
#----------------------------------------------------  
USER $NB_USER  
  
# Make sure that necessary packages are installed  
RUN conda create -yq -n python2 python=2.7 ipython \  
cython \  
dipy \  
graphviz \  
joblib \  
jupyter \  
matplotlib \  
nb_conda \  
nb_conda_kernels \  
nilearn \  
notebook \  
pandas \  
pip \  
scikit-image \  
seaborn && \  
conda clean -tipsy  
  
# Make sure that Python2 is loaded before Python3  
ENV PATH=/opt/conda/envs/python2/bin:$PATH  
  
# Import matplotlib the first time to build the font cache.  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg $CONDA_DIR/envs/python2/bin/python -c "import
matplotlib.pyplot"  
  
# Activate ipywidgets extension in the environment that runs the notebook
server  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
# Install Python 2 kernel spec globally to avoid permission problems when
NB_UID  
# switching at runtime and to allow the notebook server running out of the
root  
# environment to find it. Also, activate the python2 environment upon kernel  
# launch.  
USER root  
RUN pip install kernda --no-cache && \  
$CONDA_DIR/envs/python2/bin/python -m ipykernel install && \  
kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json && \  
pip uninstall kernda -y  
  
#---------------------------------------------  
# Install graphviz and update pip dependencies  
#---------------------------------------------  
USER root  
RUN apt-get install -yq --no-install-recommends graphviz  
USER $NB_USER  
RUN pip install --upgrade --quiet pip && \  
pip install --upgrade --quiet nipy \  
rdflib \  
pprocess \  
\--ignore-installed && \  
rm -rf ~/.cache/pip  
  
#------------------------------------------  
# Install newest version of Nipype (github)  
#------------------------------------------  
USER $NB_USER  
# Install Nipype dependencies  
RUN conda install -yq -n python2 nipype  
  
# Remove Nipype and install newest version from github  
RUN conda remove -yq -n python2 nipype && \  
easy_install --upgrade nipype  
  
#---------------------  
# Install FSL and AFNI  
#---------------------  
USER root  
RUN apt-get update && \  
apt-get install -y -qq --no-install-recommends fsl-core fsl-atlases afni  
ENV FSLDIR=/usr/share/fsl/5.0 \  
FSLOUTPUTTYPE=NIFTI_GZ \  
FSLMULTIFILEQUIT=TRUE \  
POSSUMDIR=/usr/share/fsl/5.0 \  
LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH \  
FSLTCLSH=/usr/bin/tclsh \  
FSLWISH=/usr/bin/wish \  
AFNI_MODELPATH=/usr/lib/afni/models \  
AFNI_IMSAVE_WARNINGS=NO \  
AFNI_TTATLAS_DATASET=/usr/share/afni/atlases \  
AFNI_PLUGINPATH=/usr/lib/afni/plugins \  
PATH=/usr/lib/fsl/5.0:/usr/lib/afni/bin:$PATH  
  
#---------------------  
# Install ANTs and C3D  
#---------------------  
USER root  
RUN mkdir -p /opt/ants && \  
curl -sSL
"https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Debian_jessie_x64.tar.bz2"
\  
| tar -xjC /opt/ants --strip-components 1  
  
ENV ANTSPATH=/opt/ants  
ENV PATH=$ANTSPATH:$PATH  
  
# Installing and setting up c3d  
RUN mkdir -p /opt/c3d && \  
curl -sSL
"http://downloads.sourceforge.net/project/c3d/c3d/1.0.0/c3d-1.0.0-Linux-x86_64.tar.gz"
\  
| tar -xzC /opt/c3d --strip-components 1  
  
ENV C3DPATH=/opt/c3d/  
ENV PATH=$C3DPATH/bin:$PATH  
  
#---------------------------  
# Install FreeSurfer (v.6.0)  
#---------------------------  
USER root  
RUN wget -q
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-
centos6_x86_64-stable-pub-v6.0.0.tar.gz  
RUN tar -xvzf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz \  
-C /opt \  
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
\--exclude='freesurfer/lib/qt'  
RUN rm freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz  
  
ENV FSL_DIR=/usr/share/fsl/5.0 \  
OS=Linux \  
FS_OVERRIDE=0 \  
FIX_VERTEX_AREA= \  
FSF_OUTPUT_FORMAT=nii.gz \  
FREESURFER_HOME=/opt/freesurfer  
ENV SUBJECTS_DIR=$FREESURFER_HOME/subjects \  
FUNCTIONALS_DIR=$FREESURFER_HOME/sessions \  
MNI_DIR=$FREESURFER_HOME/mni \  
LOCAL_DIR=$FREESURFER_HOME/local \  
FSFAST_HOME=$FREESURFER_HOME/fsfast \  
MINC_BIN_DIR=$FREESURFER_HOME/mni/bin \  
MINC_LIB_DIR=$FREESURFER_HOME/mni/lib \  
MNI_DATAPATH=$FREESURFER_HOME/mni/data \  
FMRI_ANALYSIS_DIR=$FREESURFER_HOME/fsfast  
ENV PERL5LIB=$MINC_LIB_DIR/perl5/5.8.5 \  
MNI_PERL5LIB=$MINC_LIB_DIR/perl5/5.8.5 \  
PATH=$FREESURFER_HOME/bin:$FSFAST_HOME/bin:$FREESURFER_HOME/tktools:$MINC_BIN_DIR:$PATH  
RUN echo
"cHJpbnRmICJtaWNoYWVsbm90dGVyQGhvdG1haWwuY29tXG4xNDY4NVxuICpDNG9aVTJpclRmUGNcbiBGU1ByejhxQ0NXNWE2XG4iID4gL29wdC9mcmVlc3VyZmVyL2xpY2Vuc2UudHh0Cg=="
| base64 -d | sh  
  
#----------------------------------------  
# Clear apt cache and other empty folders  
#----------------------------------------  
USER root  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /boot /media /mnt /srv  

