FROM ubuntu:16.04  
  
LABEL maintainer="Erik Teichmann <kontakt.teichmann@gmail.com>"  
  
USER root  
  
ADD requirements_apt.txt /tmp/requirements_apt.txt  
ADD requirements_pip.txt /tmp/requirements_pip.txt  
ADD install_nbextensions.sh /tmp/install_nbextensions.sh  
RUN apt-get update && \  
cat /tmp/requirements_apt.txt | xargs apt-get install -y --no-install-
recommends && \  
apt-get clean && \  
pip3 install --upgrade pip && \  
pip3 install setuptools && \  
pip3 install wheel && \  
pip3 install -r /tmp/requirements_pip.txt && \  
chmod +x /tmp/install_nbextensions.sh && \  
/tmp/install_nbextensions.sh  
  
ADD matplotlibrc /usr/local/lib/python3.5/dist-packages/matplotlib/mpl-
data/matplotlibrc  
  
# Create non-root user to run jupyter  
ENV NB_USER data-science  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER  
  
EXPOSE 8888  
WORKDIR /workplace  
ENV DISPLAY :0  
  
USER $NB_USER  
RUN ipython profile create  
ADD ipython_kernel_config.py
$HOME/.ipython/profile_default/ipython_kernel_config.py  
  
CMD ["/usr/local/bin/jupyter-notebook", "--no-browser", "--port 8888", "--
ip=0.0.0.0"]  

