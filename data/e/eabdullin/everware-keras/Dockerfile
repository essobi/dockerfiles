# Container for your repository to work with everware.  
# Your analysis container should inherit this one with  
# `FROM eabdullin/everware-keras`  
FROM continuumio/anaconda  
MAINTAINER Yelaman Abdullin <a.elaman.b@gmail.com>  
  
# Install anaconda  
ENV CONDA_DIR /opt/conda  
  
RUN $CONDA_DIR/bin/conda update conda && \  
conda update --all  
  
RUN /bin/bash -c "ipython kernelspec install-self"  
  
RUN pip install git+git://github.com/Theano/Theano.git && \  
pip install git+git://github.com/fchollet/keras.git  
  
RUN mkdir -p /srv/  
WORKDIR /srv/  
  
# fetch juptyerhub-singleuser entrypoint  
ADD
https://raw.githubusercontent.com/jupyter/jupyterhub/master/scripts/jupyterhub-
singleuser /usr/local/bin/jupyterhub-singleuser  
RUN chmod 755 /usr/local/bin/jupyterhub-singleuser  
  
# jupyter is our user  
RUN useradd -m -s /bin/bash jupyter  
  
USER jupyter  
ENV HOME /home/jupyter  
ENV SHELL /bin/bash  
ENV USER jupyter  
  
WORKDIR /home/jupyter/  
  
EXPOSE 8888  
ADD singleuser.sh /srv/singleuser/singleuser.sh  
CMD ["sh", "/srv/singleuser/singleuser.sh"]

