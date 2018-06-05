FROM continuumio/anaconda3  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
build-essential \  
byobu \  
gcc \  
git-core git \  
htop \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN conda update -n base conda  
RUN conda install -y -c conda-forge bcolz keras  
RUN conda install pytorch-cpu torchvision-cpu -c pytorch  
RUN conda install -y dask  
  
# Install Python packages  
RUN pip --no-cache-dir install --upgrade \  
astor \  
altair \  
fastai \  
gensim \  
graphviz \  
h5py \  
hdfs \  
isoweek \  
jsonpath_rw_ext \  
jupyter_contrib_nbextensions \  
ktext \  
more_itertools \  
nmslib \  
opencv-python \  
pandas_summary \  
pyhive \  
spacy \  
sklearn_pandas \  
tensorflow-hub \  
tqdm \  
wget  
  
# Open Ports for TensorBoard, Jupyter, and SSH  
EXPOSE 6006  
EXPOSE 7654  
EXPOSE 22  
#Setup File System  
RUN mkdir ds  
ENV HOME=/ds  
ENV SHELL=/bin/bash  
VOLUME /ds  
WORKDIR /ds  
ADD run_jupyter.sh /ds/run_jupyter.sh  
RUN chmod +x /ds/run_jupyter.sh  
  
# Run the shell  
CMD [ "/bin/bash" ]  

