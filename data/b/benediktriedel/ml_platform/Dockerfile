FROM ivukotic/ml_base:latest  
  
LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>  
  
# Need to install npm and all needed pieces for jupyterhub  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g configurable-http-proxy  
  
##############################  
# Python 2 packages  
##############################  
  
RUN pip2 --no-cache-dir install \  
h5py \  
tables \  
ipykernel \  
metakernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
Pillow \  
scipy \  
sklearn \  
qtpy \  
seaborn \  
tensorflow-gpu \  
keras \  
elasticsearch \  
gym \  
graphviz \  
JSAnimation \  
holoviews[all] \  
bokeh \  
Cython  
RUN python2 -m ipykernel.kernelspec  
  
#############################  
# Python 3 packages  
#############################  
  
RUN pip3 --no-cache-dir install \  
h5py \  
tables \  
ipykernel \  
metakernel \  
jupyter \  
jupyterlab \  
jupyterhub \  
globus_sdk \  
globus_sdk[jwt] \  
matplotlib \  
numpy \  
pandas \  
Pillow \  
scipy \  
sklearn \  
qtpy \  
seaborn \  
tensorflow-gpu \  
keras \  
elasticsearch \  
gym \  
graphviz \  
JSAnimation \  
holoviews[all] \  
bokeh \  
Cython  
RUN python3 -m ipykernel.kernelspec  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  
  
COPY environment /environment  
COPY exec /.exec  
COPY run /.run  
COPY shell /.shell  
RUN chmod 755 .exec .run .shell  
RUN jupyter serverextension enable --py jupyterlab --sys-prefix  
  
RUN echo ". /environment && \  
git clone https://github.com/briedel/ML_platform_tests.git && \  
echo \"========= all set up. ============\" && \  
cd ML_platform_tests && \  
ls" | bash  
  
RUN echo "mkdir -p /data/tutorial/amir && \  
cd /data/tutorial/amir && \  
wget -N http://archive.ics.uci.edu/ml/machine-learning-
databases/00279/SUSY.csv.gz && \  
yes n | gunzip SUSY.csv.gz" | bash  
  
RUN echo "mkdir -p /data/tutorial/ilija && \  
cd /data/tutorial/ilija" | bash  
  
RUN echo "mkdir -p /data/tutorial/Ben && \  
cd /data/tutorial/Ben && \  
wget -nc https://data.mendeley.com/archiver/pvn3xc3wy5?version=1 -O
CaloGAN.zip && \  
yes n | unzip CaloGAN.zip " | bash  
  
RUN echo "mkdir -p /ML_platform_tests/tutorial/Ben && \  
cd /ML_platform_tests/tutorial/Ben && \  
git clone https://github.com/hep-lbdl/CaloGAN.git && \  
cd /ML_platform_tests/tutorial/Ben/CaloGAN/models && \  
echo \"positron: '/data/tutorial/Ben/eplus.hdf5'\" > particles.yaml" | bash  
  
RUN "cd /opt/root/ && \  
source bin/thisroot.sh && \  
mkdir -p /root/.local/share/jupyter/kernels && \  
cp -r $ROOTSYS/etc/notebook/kernels/root ~/.local/share/jupyter/kernels && \  
mkdir /root/.jupyter/" | bash  
  
# RUN wget
https://raw.githubusercontent.com/briedel/ML_platform_tests/master/jupyterhub_config.py  
RUN useradd -m jovyan  
ENV HOME=/home/jovyan  
WORKDIR $HOME  
USER jovyan  
  
#execute service  
# CMD ["/.run"]  
ENV PATH
/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
# CMD ["jupyterhub-singleuser", "--config", "jupyterhub_config.py", "--allow-
root"]  
CMD ["jupyterhub-singleuser"]  

