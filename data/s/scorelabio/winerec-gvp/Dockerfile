FROM rocker/verse:3.4.3  
LABEL maintainer="adrien@scorelab.io"  
  
ARG GITHUB_PAT  
ARG NJOBS=1  
ARG PYTHON_VER=2  
ARG FASTFM_COMMIT=3a194c1  
  
## Install apt packages  
##==============================================================================  
RUN apt-get update --fix-missing \  
&& apt-get install -y --allow-unauthenticated --no-install-recommends \  
## For CircleCI  
ca-certificates \  
git \  
gzip \  
ssh \  
tar \  
## For R packages  
libglu1-mesa-dev \  
libpng-dev \  
## For conda install  
bzip2 \  
wget  
  
## clean apt  
RUN apt-get purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/log/dpkg.log  
  
## Install miniconda3  
## https://hub.docker.com/r/conda/miniconda3/~/dockerfile/  
## https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/  
##==============================================================================  
ENV CONDA_DIR=/opt/conda  
  
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
-O /tmp/miniconda.sh \  
&& /bin/bash /tmp/miniconda.sh -bfp ${CONDA_DIR} \  
&& rm -rf /tmp/miniconda.sh  
  
## add conda to PATH  
ENV PATH=${CONDA_DIR}/bin:$PATH  
  
## add channels. the latest has the highest priority  
RUN conda config --add channels conda-forge \  
&& conda config --add channels anaconda  
  
## Install python and pip  
##==============================================================================  
RUN conda update -y conda \  
&& conda install -y \  
python=${PYTHON_VER} \  
pip  
  
## Install python fastFM (adrtod's fork)  
##==============================================================================  
## To rebuild the image with latest fastFM, use:  
## docker build --build-arg FASTFM_COMMIT=`git ls-remote
https://github.com/adrtod/fastFM.git refs/heads/master | cut -c1-7`  
## https://stackoverflow.com/questions/35154219/rebuild-docker-image-from-
specific-step  
## https://stackoverflow.com/questions/15677439/command-to-get-latest-git-
commit-hash-from-a-branch  
RUN FASTFM_COMMIT=${FASTFM_COMMIT} git clone \--recursive
https://github.com/adrtod/fastFM.git \  
&& cd fastFM \  
&& conda install -y --file requirements.txt \  
&& make -j${NJOBS} \  
&& pip install . \  
&& cd .. \  
&& rm -rf fastFM  
  
## Install other python dependencies  
##==============================================================================  
COPY requirements.txt ./  
RUN conda install -y --file requirements.txt \  
&& rm requirements.txt  
  
## Allow conda and pip install to staff group  
##==============================================================================  
RUN chown -R root:staff ${CONDA_DIR} \  
&& chmod -R g+w ${CONDA_DIR}  
  
## Install R dependencies  
##==============================================================================  
## Settings for R at startup  
RUN echo "PATH=${PATH}" >> `R RHOME`/etc/Renviron \  
&& echo "options(Ncpus = ${NJOBS})" >> `R RHOME`/etc/Rprofile.site  
  
ENV RPYTHON_PYTHON_VERSION=${PYTHON_VER}  
  
COPY requirements.r ./  
RUN R -q -e "source('requirements.r')" \  
&& rm requirements.r  
  
## Add normal user (member of staff group)  
##==============================================================================  
ENV USER=rstudio  
  
# use ROOT=TRUE for sudoer privileges  
RUN export ROOT=TRUE \  
&& bash /etc/cont-init.d/userconf  
  
#RUN export ADD=shiny \  
# && bash /etc/cont-init.d/add  
## Install winerec-gvp  
##==============================================================================  
ENV HOME=/home/${USER}  
COPY . ${HOME}/winerec-gvp  
RUN chown -R ${USER}:${USER} ${HOME}/winerec-gvp  
  
## switch to normal user  
USER ${USER}  
  
WORKDIR ${HOME}/winerec-gvp  
  
## create .env file  
RUN cp docker.env .env  
  
CMD make run_all  

