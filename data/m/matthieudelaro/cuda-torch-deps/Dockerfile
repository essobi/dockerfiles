# based on https://github.com/Kaixhin/dockerfiles/blob/master/cuda-
torch/cuda_v7.5/deps/Dockerfile,  
# but uses images from Nvidia, to leverage Nvidia Docker Plugin + Nut
(https://github.com/matthieudelaro/nut/)  
FROM nvidia/cuda:7.5-cudnn4-devel  
  
# Install git, apt-add-repository and dependencies for iTorch  
RUN apt-get update && apt-get install -y \  
git \  
software-properties-common \  
ipython3 \  
libssl-dev \  
libzmq3-dev \  
python-zmq \  
python-pip  
  
# Install Jupyter Notebook for iTorch  
RUN pip install notebook ipywidgets  
  
# Run Torch7 installation scripts (dependencies only)  
RUN git clone https://github.com/torch/distro.git /root/torch --recursive &&
cd /root/torch && \  
bash install-deps  

