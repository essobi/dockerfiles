FROM jupyter/scipy-notebook  
MAINTAINER https://twitter.com/yacchin1205  
  
USER root  
  
### Japanese fonts  
RUN apt-get update && apt-get install -y fonts-takao  
  
### PyMC  
RUN conda install --quiet --yes pymc && \  
conda install --quiet --yes -c conda-forge pymc3  
  
### Prepare PIP  
RUN conda install --quiet --yes pip && \  
pip install --upgrade -I setuptools  
  
### for Google BigQuery  
RUN pip install --upgrade google-api-python-client oauth2client  
  
### for Google DataStore  
RUN pip install --upgrade google-cloud-datastore  
  
### for analyzing EEG data  
RUN pip install --upgrade mne  
  
### for py-pursuit  
RUN pip install git+https://github.com/yacchin1205/py-pursuit.git  
  
### for AutoPrait  
RUN git clone https://github.com/abbshr/implement-of-AutoPlait-algorithm.git
/tmp/autoplait && \  
cd /tmp/autoplait/codes/autoplait/ && make && \  
mv /tmp/autoplait/codes/autoplait /opt/  
  
### for TensorFlow with Keras  
RUN pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.1-cp36-cp36m-linux_x86_64.whl
&& \  
pip install keras  
  
### for python-fitbit  
RUN git clone https://github.com/orcasgit/python-fitbit /tmp/python-fitbit &&
\  
cd /tmp/python-fitbit && \  
pip install -r requirements/base.txt && \  
pip install -r requirements/dev.txt && \  
pip install -r requirements/test.txt && \  
python3 setup.py install  
  
### for pymongo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.4.list && \  
apt-get update && \  
apt-get install -y mongodb-org && \  
pip install pymongo  
  
### for misfit  
RUN apt-get update && apt-get install -y libssl-dev && pip install --upgrade
geopy misfit  
  
### for hmmlearn  
RUN pip install hmmlearn  
  
### for basemap  
RUN cd /tmp && wget
https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz && \  
tar xf v1.0.7rel.tar.gz && \  
cd /tmp/basemap-1.0.7rel/geos-3.3.3 && \  
./configure && make && make install && \  
cd /tmp/basemap-1.0.7rel && pip install .  
  
# extensions for jupyter  
## nbextensions_configurator  
RUN pip install jupyter_nbextensions_configurator && \  
pip install six git+https://github.com/ipython-
contrib/jupyter_contrib_nbextensions.git  
  
# Theme for jupyter  
ADD conf /tmp/  
USER $NB_USER  
RUN mkdir -p $HOME/.jupyter/custom/ && \  
cp /tmp/custom.css $HOME/.jupyter/custom/custom.css  
  
RUN mkdir -p $HOME/.local/share && \  
jupyter nbextensions_configurator enable \--user && \  
jupyter contrib nbextension install --user  

