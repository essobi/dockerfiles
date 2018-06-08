FROM tensorflow/tensorflow:latest-gpu-py3  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NB_USER mdp  
ENV NB_UID 6000  
ENV DATA_DIR /data  
ENV WORK_DIR /src  
ENV HOME /home/$NB_USER  
ENV NOTEBOOK_DIR /home/$NB_USER/notebooks  
  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
vim \  
jed \  
emacs \  
nano \  
wget \  
cmake \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install TensorFlow CPU version from central repo  
RUN pip --no-cache-dir install \  
nltk  
  
# Create NB_UID user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER \  
&& mkdir -p $WORK_DIR $DATA_DIR $NOTEBOOK_DIR \  
&& chown $NB_USER $HOME $WORK_DIR $DATA_DIR $NOTEBOOK_DIR \  
&& ln -s $WORK_DIR $HOME$WORK_DIR \  
&& ln -s $DATA_DIR $HOME$DATA_DIR \  
&& ln -s $NOTEBOOK_DIR $DATA_DIR/notebooks  
  
USER $NB_USER  
WORKDIR $NOTEBOOK_DIR  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]

