# ninjaben/jupyter-hub-oauth-matlab  
#  
# JupyterHub plus Google OAuth, plus support for a mounted-in Matlab
installatoin and the Jypyter matlab_kernel.  
#  
# Example usage:  
# docker run --rm -p 80:8000 --rm -v
/usr/local/MATLAB/R2016a:/usr/local/MATLAB/from-host -v
/home/ben/Desktop/matlab-docker:/var/log/matlab --mac-
address=68:f7:28:f6:68:a6 ninjaben/jupyter-matlab-support  
#  
# This example worked on the author's dev machine. To run it on your machine
you must make some substitutions:  
# - For "/usr/local/MATLAB/R2016a" substitute your Matlab location and
version. Try "ls -al `which matlab`".  
# - For "/home/ben/Desktop/matlab-docker", substitute any folder where you
want the container to write logs.  
# - For "68:f7:28:f6:68:a6", substitute the mac address associated with your
Matlab license.  
#  
# Based on work by Michael Perry at Stanford. Thanks!  
# Based on the JupyterHub official oauthenticator example. Thanks!  
# https://github.com/jupyterhub/oauthenticator/tree/master/example  
#  
FROM ninjaben/jupyter-hub-oauth  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
# Matlab and Python dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
python-dev \  
gfortran \  
pkg-config \  
libpng12-dev \  
libfreetype6-dev \  
libblas-dev \  
liblapack-dev \  
xorg \  
xorg-dev \  
nano \  
vim \  
emacs  
  
# Python libs  
RUN pip install pyzmq \  
&& pip install matplotlib \  
&& pip install numpy \  
&& pip install scipy \  
&& pip install nibabel \  
&& pip install pymatbridge \  
&& pip install jupyter \  
&& pip install jupyter_client \  
&& pip install matlab_kernel \  
&& python -m matlab_kernel install  
  
# wrapper to start mounted-in matlab, plus MATLABPATH=/usr/local/MATLAB/  
ADD matlab /usr/local/bin/matlab  
  
# shared temp folder where jupyter users (via python-matlab bridge) will read
and write image files  
RUN mkdir /tmp/MatlabData  
  
# hack alert! explicitly create files that jupyter users (via python-matlab
bridge) may overwrite  
# would prefer to use file system acl on /tmp/MatlabData, but don't want to
mess with fstab  
# or would prefer to use g+rws on /tmp/MatlabData, but can't get jupyterhub to
set umask 002 for users  
# so for now, just create explicitly and explicitly open permissions to
jupyter group  
# an even better solution would be to use user-specific temp folders and/or
UUID file names  
RUN for n in $(seq -f "%03g" 0 100); do touch /tmp/MatlabData/MatlabFig$n.png;
done;  
RUN chown -R root:jupyter /tmp/MatlabData \  
&& chmod -R 775 /tmp/MatlabData  
  
# shared Matlab demo notebook  
ADD MatlabWelcome.ipynb /srv/ipython/examples/MatlabWelcome.ipynb  
  
# update jupyter config file with some changes for matlab  
ADD jupyterhub_config.py /srv/oauthenticator/jupyterhub_config.py  
  
# get the "toolbox toolbox" which helps manage Matlab toolboxes  
ADD toolbox-toolbox/ /srv/toolbox-toolbox/  
  
# add toolboxes to Matlab path at startup  
ADD startup.m /usr/local/MATLAB/startup.m  
  
# wrapper to create user notebook dir and fetch notebooks launching user's
jupyter server  
ADD matlab-setup-jupyterhub-singleuser /srv/matlab-setup-jupyterhub-singleuser  
  

