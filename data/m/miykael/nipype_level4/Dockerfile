# This Dockerfile is based on the dockerfile 'fmriprep' from the Poldrack  
# Lab (https://github.com/poldracklab/fmriprep). The jupyter notebook
foundation  
# is based on jupyter/docker-stacks's base-notebook.  
#  
# This means that the same copyrights apply to this Dockerfile, as they do for  
# the above mentioned dockerfiles. For more information see:  
# https://github.com/miykael/nipype_env  
  
FROM miykael/nipype_level3  
MAINTAINER Michael Notter <michaelnotter@hotmail.com>  
  
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

