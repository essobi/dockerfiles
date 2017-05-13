FROM ubuntu:trusty
# DON'T FORGET TO SET ENV DOCKER_IMAGE="fliem/lhab_docker:vXXXXX"
#### Install the validator
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get remove -y curl && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN npm install -g bids-validator@0.18.17

RUN apt-get update && \
    apt-get install -y tcsh bc tar libgomp1 perl-modules curl wget htop tree git unzip cmake

#### FSL
RUN apt-get update && \
  wget -O- http://neuro.debian.net/lists/trusty.de-md.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list && \
  sudo apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9 && \
  apt-get update && \
  apt-get install -y fsl-core=5.0.9-3~nd14.04+1

# Configure environment
ENV FSLDIR=/usr/share/fsl/5.0
ENV FSLOUTPUTTYPE=NIFTI_GZ
ENV PATH=/usr/lib/fsl/5.0:$PATH
ENV FSLMULTIFILEQUIT=TRUE
ENV POSSUMDIR=/usr/share/fsl/5.0
ENV LD_LIBRARY_PATH=/usr/lib/fsl/5.0:$LD_LIBRARY_PATH
ENV FSLTCLSH=/usr/bin/tclsh
ENV FSLWISH=/usr/bin/wish
ENV FSLOUTPUTTYPE=NIFTI_GZ


#### ANTS
RUN apt-get update && \
    mkdir -p /opt/ants && \
    curl -sSL "https://github.com/stnava/ANTs/releases/download/v2.1.0/Linux_Ubuntu14.04.tar.bz2" \
    | tar -xjC /opt/ants --strip-components 1

ENV ANTSPATH=/opt/ants
ENV PATH=$ANTSPATH:$PATH


#### AFNI
RUN apt-get update && \
    apt-get install -y afni

#### FreeSurfer
RUN apt-get -y update && \
    wget -qO- ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/5.3.0-HCP/freesurfer-Linux-centos4_x86_64-stable-pub-v5.3.0-HCP.tar.gz | tar zxv -C /opt \
    --exclude='freesurfer/trctrain' \
    --exclude='freesurfer/subjects/fsaverage_sym' \
    --exclude='freesurfer/subjects/fsaverage3' \
    --exclude='freesurfer/subjects/fsaverage4' \
    --exclude='freesurfer/subjects/fsaverage5' \
    --exclude='freesurfer/subjects/fsaverage6' \
    --exclude='freesurfer/subjects/cvs_avg35' \
    --exclude='freesurfer/subjects/cvs_avg35_inMNI152' \
    --exclude='freesurfer/subjects/bert' \
    --exclude='freesurfer/subjects/V1_average' \
    --exclude='freesurfer/average/mult-comp-cor' \
    --exclude='freesurfer/lib/cuda' \
    --exclude='freesurfer/lib/qt'

RUN /bin/bash -c 'touch /opt/freesurfer/.license'

# Set up the environment
ENV OS=Linux
ENV FS_OVERRIDE=0
ENV FIX_VERTEX_AREA=
ENV SUBJECTS_DIR=/opt/freesurfer/subjects
ENV FSF_OUTPUT_FORMAT=nii.gz
ENV MNI_DIR=/opt/freesurfer/mni
ENV LOCAL_DIR=/opt/freesurfer/local
ENV FREESURFER_HOME=/opt/freesurfer
ENV FSFAST_HOME=/opt/freesurfer/fsfast
ENV MINC_BIN_DIR=/opt/freesurfer/mni/bin
ENV MINC_LIB_DIR=/opt/freesurfer/mni/lib
ENV MNI_DATAPATH=/opt/freesurfer/mni/data
ENV FMRI_ANALYSIS_DIR=/opt/freesurfer/fsfast
ENV PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
ENV MNI_PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
ENV PATH=/opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH


#### DCM2NIIX
WORKDIR /root
RUN apt-get update && \
    apt-get install -y pkg-config libyaml-cpp-dev libyaml-cpp0.5 cmake libboost-dev
RUN wget https://github.com/rordenlab/dcm2niix/archive/v1.0.20161101.zip -O dcm2niix.zip && unzip dcm2niix.zip && rm dcm2niix.zip
RUN cd dcm2niix-* && cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr/ . && make install
RUN cd .. #&& rm -r dcm2niix*

#### PYTHON / NIPYPE
RUN apt-get update && \
    apt-get install -y graphviz pandoc

WORKDIR /root

# Install anaconda
RUN echo 'export PATH=/usr/local/anaconda:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh -O anaconda.sh && \
    /bin/bash anaconda.sh -b -p /usr/local/anaconda && \
    rm anaconda.sh

ENV PATH=/usr/local/anaconda/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
# Create conda environment, use nipype's conda-forge channel
RUN conda config --add channels conda-forge && \
    conda install -y lockfile nipype joblib

RUN pip install pybids
# without 'v'
#ENV LHAB_PIPE_VER="0.8.7.dev"
#RUN wget https://github.com/fliem/lhab_pipelines/archive/v${LHAB_PIPE_VER}.zip -O lhab_pipelines.zip && \
#unzip lhab_pipelines.zip -d /code/
#RUN rm lhab_pipelines.zip
#RUN mv /code/lhab_pipelines-${LHAB_PIPE_VER} /code/lhab_pipelines
ENV PYTHONPATH=/code/lhab_pipelines:$PYTHONPATH
ENV DOCKER_IMAGE="fliem/lhab_docker:v0.7"
CMD ["/bin/bash"]
