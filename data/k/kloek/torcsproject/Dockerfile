#Pull image  
FROM ubuntu:xenial  
  
#Update  
RUN apt-get update  
  
#Install git and python  
RUN apt-get install -y git \  
python-dev \  
python-pip && \  
pip install --upgrade pip  
  
#Install Keras 1.1.0  
RUN pip install https://github.com/fchollet/keras/tarball/1.1.0  
  
#Install Tensorflow  
RUN export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-
linux_x86_64.whl && \  
pip install --upgrade $TF_BINARY_URL  
  
#Dependencies for gym-torcs  
RUN apt-get install -y xautomation \  
libglib2.0-dev \  
libgl1-mesa-dev \  
libglu1-mesa-dev \  
freeglut3-dev \  
libplib-dev \  
libopenal-dev \  
libalut-dev \  
libxi-dev \  
libxmu-dev \  
libxrender-dev \  
libxrandr-dev \  
libpng12-dev && \  
pip install gym && \  
pip install numpy && \  
pip install h5py  
  
# Install dependecies for Python3  
RUN apt-get install -y python3-pip  
RUN apt-get install -y python3-tk  
  
RUN pip3 install gym && \  
pip3 install tensorflow && \  
pip3 install matplotlib  
  
#Install gym_torcs  
RUN git clone https://github.com/kloek/gym_torcs.git && \  
cd gym_torcs/vtorcs-RL-color && \  
./configure && \  
make && \  
make install && \  
make datainstall && \  
cd ../..  
  
#Do what the install.sh does in TorcsProject  
RUN git clone https://github.com/kloek/TorcsProject.git && \  
cd TorcsProject && \  
git log -n 1 > ../gym_torcs/agent_version && \  
git status >> ../gym_torcs/agent_version && \  
rm -rf ../gym_torcs/agents && \  
cp -r agents ../gym_torcs/agents && \  
rm -rf ../gym_torcs/run_ddpg.py && \  
cp run_ddpg.py ../gym_torcs/ && \  
rm -rf ../gym_torcs/config.py && \  
cp config.py ../gym_torcs/ && \  
cd ..  
  
#Configuring Display and AspectJ  
RUN apt-get install -y default-jdk \  
aspectj  
  
RUN apt-get install screen  
  
RUN apt-get install -y x11vnc xvfb  
RUN mkdir ~/.vnc  
  
RUN echo "export DISPLAY=:1.0" >> .bashrc  
  
ADD practice.xml ~/.torcs/config/raceman  
ADD practice.xml /usr/local/share/games/torcs/config/raceman  
  
ADD screen.xml ~/.torcs/config  
ADD screen.xml /usr/local/share/games/torcs/config  
  
EXPOSE 80  
ADD entrypoint.sh /  
ENTRYPOINT /entrypoint.sh ; /bin/bash  
  
WORKDIR gym_torcs/  

