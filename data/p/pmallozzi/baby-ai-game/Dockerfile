FROM consol/ubuntu-xfce-vnc:1.1.0  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 USER=$USER HOME=$HOME  
  
RUN echo "The working directory is: $HOME"  
RUN echo "The user is: $USER"  
  
USER 0  
EXPOSE 5901  
EXPOSE 6901  
EXPOSE 8097  
RUN apt-get update && apt-get install -y \  
sudo \  
git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install dependencies  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
apt-utils \  
curl \  
nano \  
vim \  
git \  
zlib1g-dev \  
cmake \  
python-software-properties \  
software-properties-common \  
graphviz \  
libgraphviz-dev \  
graphviz-dev \  
pkg-config  
  
# Install python  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python-numpy \  
python-dev  
  
# Installing python3.6  
RUN add-apt-repository ppa:jonathonf/python-3.6  
RUN apt update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python3.6 \  
python3.6-dev \  
python3.6-venv  
  
## It causes problems TODO:Fix distutils installation  
#RUN apt update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
# python3.6-distutils  
RUN ln -s /usr/bin/python3.6 /usr/local/bin/python3  
  
# Installing pip and pip3  
RUN apt-get remove python-pip python3-pip  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN python3 get-pip.py  
RUN rm get-pip.py  
  
RUN mkdir -p $HOME  
WORKDIR $HOME  
  
# Cloning the repositories  
RUN git clone https://github.com/pierg/baby-ai-game.git -b dev --single-branch  
RUN git clone https://github.com/pierg/gym-minigrid.git -b dev --single-branch  
  
RUN pip3 install --upgrade pip  
RUN pip install --upgrade pip  
  
# Installing Torch  
RUN pip3 install
http://download.pytorch.org/whl/cpu/torch-0.3.1-cp36-cp36m-linux_x86_64.whl  
RUN pip3 install torchvision  
  
RUN pip3 install -r ./baby-ai-game/requirements.txt  
  
WORKDIR $HOME/baby-ai-game  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD [""]  

