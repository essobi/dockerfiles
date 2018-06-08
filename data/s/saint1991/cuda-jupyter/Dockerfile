FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04  
ENV LANG C.UTF-8  
# install python and pip  
RUN \  
build_deps='software-properties-common wget' && \  
apt-get update -y && \  
apt-get install -y ${build_deps} && \  
add-apt-repository ppa:jonathonf/python-3.6 && \  
apt-get update -y && \  
apt-get install -y \  
libgomp1 \  
python3.6 && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
apt-get purge -y ${build_deps} && \  
apt-get autoclean && \  
rm -rf get-pip.py /var/lib/apt/lists/*  
  
# install jupyter  
RUN \  
python3 -m pip install --upgrade pip && \  
python3 -m pip install jupyter && \  
ipython kernel install  
  
COPY jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py  
  
# add a user jupyter  
RUN useradd -ms /bin/bash jupyter  
USER jupyter  
WORKDIR /home/jupyter  
  
RUN mkdir data  
VOLUME /home/jupyter/data  
  
EXPOSE 8888  
ENTRYPOINT [ "jupyter", "notebook" ]  
CMD [ "--config=/etc/jupyter/jupyter_notebook_config.py" ]  

