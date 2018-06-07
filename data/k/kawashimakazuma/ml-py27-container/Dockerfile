# TensorFlow & scikit-learn with Pythonxx  
#FROM python:3.6  
FROM python:2.7  
LABEL maintainer “kazuma<gs2safari'a'gmail.com>”  
  
#RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"  
#RUN echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" |
sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
#RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key
add -  
#RUN apt-get update && sudo apt-get install google-cloud-sdk  
#RUN sudo apt-get install google-cloud-sdk-datalab  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libblas-dev \  
liblapack-dev\  
libatlas-base-dev \  
mecab \  
mecab-naist-jdic \  
libmecab-dev \  
gfortran \  
libav-tools \  
python-setuptools \  
python-pip \  
python-dev  
  
#RUN easy_install -U pip  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install TensorFlow CPU version  
#ENV TENSORFLOW_VERSION 1.2.1  
RUN pip --no-cache-dir install \  
#
http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.3.0-cp27-none-
linux_x86_64.whl  
#RUN pip install --upgrade tensorflow  
#tf_nightly-1.head-cp27-none-linux_x86_64  
#https://ci.tensorflow.org/view/tf-nightly/job/tf-nightly-
linux/TF_BUILD_IS_OPT=OPT,TF_BUILD_IS_PIP=PIP,TF_BUILD_PYTHON_VERSION=PYTHON2,label=cpu-#slave/lastSuccessfulBuild/artifact/pip_test/whl/tf_nightly-1.head-
cp27-none-linux_x86_64.whl  
#RUN pip install tf-nightly  
# Install Python library for Data Science  
RUN pip --no-cache-dir install \  
keras \  
sklearn \  
jupyter \  
ipykernel \  
scipy \  
simpy \  
matplotlib \  
numpy \  
pandas \  
plotly \  
sympy \  
mecab-python \  
librosa \  
Pillow \  
h5py \  
google-api-python-client \  
cloudmlmagic \  
&& \  
python -m ipykernel.kernelspec  
  
RUN git clone https://www.github.com/datalogai/recurrentshop.git  
  
WORKDIR recurrentshop  
RUN python ./setup.py install  
RUN cd ..  
RUN pip install git+https://github.com/farizrahman4u/seq2seq.git  
  
# Set up Jupyter Notebook config  
ENV CONFIG /root/.jupyter/jupyter_notebook_config.py  
ENV CONFIG_IPYTHON /root/.ipython/profile_default/ipython_config.py  
  
RUN jupyter notebook --generate-config --allow-root && \  
ipython profile create  
  
RUN echo "c.NotebookApp.ip = '*'" >>${CONFIG} && \  
echo "c.NotebookApp.open_browser = False" >>${CONFIG} && \  
echo "c.NotebookApp.iopub_data_rate_limit=10000000000" >>${CONFIG} && \  
echo "c.MultiKernelManager.default_kernel_name = 'python2'" >>${CONFIG}  
  
RUN echo "c.InteractiveShellApp.exec_lines = ['%matplotlib inline']"
>>${CONFIG_IPYTHON}  
  
# Copy sample notebooks.  
COPY notebooks /notebooks  
  
# port  
EXPOSE 8888 6006  
VOLUME /notebooks  
  
# Run Jupyter Notebook  
WORKDIR "/notebooks"  
CMD ["jupyter","notebook", "--allow-root"]  

