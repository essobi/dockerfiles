# Use Ubuntu 16.04 LTS  
FROM ubuntu:xenial-20161213  
# Pre-cache neurodebian key  
COPY docker/files/neurodebian.gpg /root/.neurodebian.gpg  
  
# Prepare environment  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
bzip2 \  
ca-certificates \  
xvfb \  
cython3 \  
build-essential \  
autoconf \  
libtool \  
pkg-config && \  
curl -sSL http://neuro.debian.net/lists/xenial.us-ca.full >>
/etc/apt/sources.list.d/neurodebian.sources.list && \  
apt-key add /root/.neurodebian.gpg && \  
(apt-key adv --refresh-keys --keyserver hkp://ha.pool.sks-keyservers.net
0xA5D32F012649A5A9 || true) && \  
apt-get update  
  
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
AFNI_PLUGINPATH=/usr/lib/afni/plugins  
ENV PATH=/usr/lib/fsl/5.0:/usr/lib/afni/bin:$PATH  
  
  
ENV C3DPATH /opt/c3d/  
ENV PATH $C3DPATH/bin:$PATH  
  
ENV PATH=/opt/ICA-AROMA-0.4-beta:$PATH  
  
# Installing and setting up miniconda  
RUN curl -sSLO
https://repo.continuum.io/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh && \  
bash Miniconda3-4.3.11-Linux-x86_64.sh -b -p /usr/local/miniconda && \  
rm Miniconda3-4.3.11-Linux-x86_64.sh  
  
ENV PATH=/usr/local/miniconda/bin:$PATH \  
LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
# Installing precomputed python packages  
RUN conda install -y mkl=2017.0.1 mkl-service && \  
conda install -y numpy=1.12.0 \  
scipy=0.18.1 \  
scikit-learn=0.18.1 \  
matplotlib=2.0.0 \  
pandas=0.19.2 \  
libxml2=2.9.4 \  
libxslt=1.1.29\  
traits=4.6.0 && \  
chmod +x /usr/local/miniconda/bin/*  
  
# Precaching fonts  
RUN python -c "from matplotlib import font_manager"  
  
# Installing Ubuntu packages and cleaning up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
git=1:2.7.4-0ubuntu1 \  
graphviz=2.38.0-12ubuntu2 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Unless otherwise specified each process should only use one thread - nipype  
# will handle parallelization  
ENV MKL_NUM_THREADS=1 \  
OMP_NUM_THREADS=1  
# Installing dev requirements (packages that are not in pypi)  
WORKDIR /root/  
ADD requirements.txt requirements.txt  
RUN pip wheel --wheel-dir=/tmp -r requirements.txt  
RUN pip install --no-index --find-links=/tmp -r requirements.txt  
  
# Installing FMRIPREP  
COPY . /root/src/fmriprep  
RUN cd /root/src/fmriprep && \  
pip wheel --wheel-dir=/tmp .[all] && \  
pip install --no-index --find-links=/tmp .[all]  
  
# Precaching atlases  
RUN mkdir /niworkflows_data  
ENV CRN_SHARED_DATA /niworkflows_data  
RUN python -c 'from niworkflows.data.getters import get_mni_template_ras;
get_mni_template_ras()' && \  
python -c 'from niworkflows.data.getters import get_mni_icbm152_nlin_asym_09c;
get_mni_icbm152_nlin_asym_09c()' #&& \  
python -c 'from niworkflows.data.getters import get_ants_oasis_template_ras;
get_ants_oasis_template_ras()'  
  
RUN ldconfig  
  
WORKDIR /root/src/fmriprep  
  
# Change permissions of wheel files  
WORKDIR /usr/local/miniconda/bin  
RUN python /usr/local/miniconda/bin/fmriprep -h > /dev/null 2>&1  
RUN chmod +x /usr/local/miniconda/lib/python3.6/site-packages/*  
RUN ldconfig  
ENTRYPOINT ["/usr/local/miniconda/bin/fmriprep"]  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="FMRIPREP" \  
org.label-schema.description="FMRIPREP - robust fMRI preprocessing tool" \  
org.label-schema.url="http://fmriprep.readthedocs.io" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/poldracklab/fmriprep" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  

