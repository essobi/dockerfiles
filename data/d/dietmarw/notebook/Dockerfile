# Base image of the IPython/Jupyter notebook, with conda  
# Intended to be used in a tmpnb installation  
# Based on https://github.com/jupyter/docker-demo-images  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:0.9.22  
MAINTAINER Dietmar Winkler <dietmar.winkler@dwe.no>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
USER root  
  
# Make sure apt is up to date  
RUN add-apt-repository 'deb http://build.openmodelica.org/apt xenial nightly'  
RUN curl -s http://build.openmodelica.org/apt/openmodelica.asc | apt-key add -  
RUN apt-get update --fix-missing && apt-get upgrade -y -o Dpkg::Options::="--
force-confold"  
  
# Install OpenModelica components  
#RUN apt-get install -y omc omlib-modelica-3.2.2 omniorb python-omniorb
omniidl omniidl-python  
RUN apt-get install -y omc omlib-modelica-3.2.2  
  
# Install rest of base system  
RUN apt-get install -y \  
bzip2 \  
ca-certificates \  
ffmpeg \  
git \  
git-sh \  
# inkscape \  
mc \  
pandoc \  
texlive \  
texlive-latex-extra\  
texlive-xetex\  
tig #\  
# wamerican  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV CONDA_DIR /opt/conda  
  
# Install conda for the student user only (this is a single user container)  
RUN echo 'export PATH=$CONDA_DIR/bin:$PATH' > /etc/profile.d/conda.sh && \  
curl -O -s https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
/bin/bash /Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR && \  
rm Miniconda3-latest-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda install --yes conda  
  
# We run our docker images with a non-root user as a security precaution.  
# student is our user  
RUN useradd -m -s /bin/bash student  
RUN chown -R student:student $CONDA_DIR  
  
EXPOSE 8888  
USER student  
ENV HOME /home/student  
# set git-sh as default shell  
ENV SHELL /usr/bin/git-sh  
#ENV SHELL /bin/bash  
ENV USER student  
ENV PATH $CONDA_DIR/bin:$PATH  
WORKDIR $HOME  
  
# General conda installation  
RUN conda install --yes jupyter \  
matplotlib \  
numpy \  
pandas \  
scipy \  
sympy \  
terminado  
# First invoke the CACHEBUST so it can be used  
RUN echo "HELLO CACHE $CACHEBUST"  
ARG CACHEBUST=1  
RUN pip install -U git+git://github.com/OpenModelica/OMPython.git  
ARG CACHEBUST=1  
RUN pip install -U git+git://github.com/OpenModelica/jupyter-openmodelica.git  
RUN pip install version_information  
RUN conda clean -yt  
  
# # Python 2 env  
# RUN conda create -n py2 python=2 ipykernel  
# RUN /bin/bash -c "source activate py2 &&\  
# ipython kernel install --user &&\  
# pip install git+git://github.com/OpenModelica/OMPython.git &&\  
# pip install git+git://github.com/OpenModelica/jupyter-openmodelica.git &&\  
# pip install version_information &&\  
# conda install --yes jupyter \  
# matplotlib \  
# numpy \  
# pandas \  
# scipy \  
# sympy \  
# terminado"  
# # conda clean -yt"  
# # RUN /bin/bash -c "source activate py2 &&\  
# # mkdir -p $CONDA_DIR/envs/py2/etc/activate.d/ &&\  
# # echo 'export PYTHONUSERSITE=1' >>
$CONDA_DIR/envs/py2/etc/activate.d/globalsitepackage.sh"  
# # Python 3 env  
# RUN conda create -n py3 python=3 ipykernel  
# RUN /bin/bash -c "source activate py3 &&\  
# ipython kernel install --user &&\  
# pip install version_information &&\  
# conda install --yes jupyter \  
# matplotlib \  
# numpy \  
# pandas \  
# scipy \  
# sympy && \  
# conda clean -yt"  
# Workaround for issue with ADD permissions  
USER root  
  
# Let's encrypt setup  
RUN mkdir /etc/letsencrypt  
COPY fullchain.pem /etc/letsencrypt/  
COPY privkey.pem /etc/letsencrypt/  
# RUN chmod o-r /etc/letsencrypt/*  
RUN chown student:student /home/student -R  
COPY ./setup.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/setup.sh  
  
USER student  
  
# When run with orchestrate.py the following command will not be executed.  
# See '--command' option instead  
CMD /usr/local/bin/setup.sh  

