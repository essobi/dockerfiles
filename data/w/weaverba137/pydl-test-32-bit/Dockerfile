FROM ioft/i386-ubuntu:trusty  
MAINTAINER Benjamin Alan Weaver <baweaver@lbl.gov>  
#  
# Variables.  
#  
ENV testuser=travis branch=hmf-object package=weaverba137/pydl \  
python_version=3.5 conda_env=test  
#  
# Add a non-privileged user.  
#  
RUN adduser --disabled-password --gecos "" ${testuser}  
RUN chown ${testuser}:${testuser} /home/${testuser}  
#  
# Tools needed  
#  
RUN apt-get update && apt-get -y install git # graphviz texlive-latex-extra
dvipng  
#  
# Install miniconda file.  
#  
COPY Miniconda-latest-Linux-x86.sh /home/${testuser}  
RUN chmod a+x /home/${testuser}/Miniconda-latest-Linux-x86.sh  
#  
# Set user.  
#  
USER ${testuser}  
WORKDIR /home/${testuser}  
#  
# Conda setup.  
#  
RUN linux32 -- /bin/bash Miniconda-latest-Linux-x86.sh -b -p ${HOME}/miniconda  
ENV base_path=${PATH}  
# ENV PATH=/home/${testuser}/miniconda/bin:${PATH}  
RUN linux32 -- /home/${testuser}/miniconda/bin/conda config --set always_yes
yes --set changeps1 no  
RUN linux32 -- /home/${testuser}/miniconda/bin/conda create -q -n ${conda_env}
python=${python_version}  
#  
# source activate doesn't work because we're in /bin/sh, but activate only  
# supports bash & zsh  
#  
# RUN source activate test  
ENV PATH=/home/${testuser}/miniconda/envs/${conda_env}/bin:${base_path} \  
CONDA_ENV_PATH=/home/${testuser}/miniconda/envs/${conda_env} \  
CONDA_DEFAULT_ENV=${conda_env}  
RUN linux32 -- conda install -q pytest pip nomkl astropy scipy matplotlib  
# RUN linux32 -- pip install --pre --upgrade numpy  
#  
# Clone.  
#  
RUN linux32 -- git clone \--depth=50 --branch=${branch}
https://github.com/${package}.git ${package}  
WORKDIR /home/${testuser}/${package}  
RUN linux32 -- git submodule update --init --recursive  
#  
# Run test.  
#  
ENTRYPOINT ["linux32", "--"]  
CMD ["python", "setup.py", "test", "-v", "-V"]  

