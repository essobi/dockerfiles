FROM continuumio/anaconda  
  
MAINTAINER lucasko.tw@gmail.com  
  
### Install jupyter  
RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN mkdir /opt/notebooks  
ENV PATH /opt/conda/bin:$PATH  
  
## Install Python Lib  
RUN pip install elasticsearch  
RUN pip install pyes  
RUN pip install scikit-learn  
RUN /opt/conda/bin/conda install -y -c anaconda seaborn=0.7.1  
  
### Install Tensor Flow  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
python-numpy \  
python-pip \  
python-scipy \  
rsync \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
RUN pip --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
&& \  
python -m ipykernel.kernelspec  
  
ENV TENSORFLOW_VERSION 0.10.0rc0  
  
# --- DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
# These lines will be edited automatically by parameterized_docker_build.sh. #  
# COPY _PIP_FILE_ /  
# RUN pip --no-cache-dir install /_PIP_FILE_  
# RUN rm -f /_PIP_FILE_  
# Install TensorFlow CPU version from central repo  
RUN pip --no-cache-dir install \  
http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp27-none-
linux_x86_64.whl  
# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Copy sample notebooks.  
COPY notebooks /notebooks  
  
# Download sample code into projects  
ENV SAMPLE /opt/notebooks/samples  
RUN mkdir $SAMPLE  
RUN git clone https://github.com/rhiever/Data-Analysis-and-Machine-Learning-
Projects.git /opt/notebooks/samples  
  
# TensorBoard  
EXPOSE 6006  
# jupyter  
EXPOSE 8888  
WORKDIR "/notebooks"  
  

