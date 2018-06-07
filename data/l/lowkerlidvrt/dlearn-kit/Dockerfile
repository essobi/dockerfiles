FROM ubuntu:16.04  
MAINTAINER Low Ker Li <lowkerli@diverta.co.jp>  
  
ENV REFRESHED_AT 2016-05-27  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y \  
bzip2 \  
curl \  
libgtk2.0-dev \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Miniconda  
RUN echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh \  
&& curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh \  
&& /bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \  
&& rm Miniconda3-latest-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN conda install -y -c menpo -c jjhelmus \  
dlib \  
h5py \  
jupyter \  
matplotlib \  
opencv3 \  
pillow \  
tensorflow \  
&& conda clean -a  
  
# Update pip  
RUN pip --no-cache-dir install --upgrade pip  
  
RUN pip --no-cache-dir install \  
keras  
  
# Copy Keras configurations  
# (Set backend to Tensorflow)  
COPY .keras/ /root/.keras/  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /usr/local/bin/  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
ENV NOTEBOOKS_DIR /root/notebooks  
  
# Prepare directories for volumes  
RUN mkdir -p \  
${NOTEBOOKS_DIR} \  
/root/bin \  
/root/python \  
/root/data  
  
# Create mount points  
VOLUME [ \  
"${NOTEBOOKS_DIR}", \  
"/root/bin", \  
"/root/python", \  
"/root/data" \  
]  
  
# Add modules path to PYTHONPATH  
ENV PYTHONPATH $PYTHONPATH:/root/python/modules  
  
# Add bin and scripts to PATH  
ENV PATH $PATH:/root/bin:/root/python/scripts  
  
WORKDIR ${NOTEBOOKS_DIR}  
  
CMD ["run_jupyter.sh"]  

