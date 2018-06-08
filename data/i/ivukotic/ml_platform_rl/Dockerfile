FROM ivukotic/ml_base:latest  
  
LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>  
  
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
baselines \  
JSAnimation  
RUN python2 -m ipykernel.kernelspec  
  
#############################  
# Python 3 packages  
#############################  
  
RUN pip3 --no-cache-dir install \  
h5py \  
tables \  
ipykernel \  
jupyter \  
jupyterlab \  
matplotlib \  
numpy \  
pandas \  
Pillow \  
scipy \  
sklearn \  
qtpy \  
seaborn \  
keras \  
elasticsearch \  
tensorflow-gpu \  
gym \  
baselines \  
JSAnimation  
RUN python3 -m ipykernel.kernelspec  
  
# build info  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt  
  
COPY environment /environment  
COPY exec /.exec  
COPY run /.run  
COPY shell /.shell  
  
RUN chmod 755 .exec .run .shell  
  
RUN jupyter serverextension enable --py jupyterlab --sys-prefix  
  
#execute service  
CMD ["/.run"]  

