FROM ubuntu:16.04  
LABEL maintainer="david@cninone.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL "C.UTF-8"  
ENV LANGUAGE en_US:en  
  
RUN apt-get update && apt-get install -y \  
sudo \  
python2.7 \  
build-essential \  
cmake \  
curl \  
gfortran \  
git \  
graphicsmagick \  
libgraphicsmagick1-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libboost-all-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libswscale-dev \  
pkg-config \  
python-dev \  
python-numpy \  
python-protobuf\  
software-properties-common \  
zip \  
libssl-dev \  
libffi-dev \  
python-pip \  
python-nose \  
python-scipy \  
python-pandas \  
python-openssl \  
wget \  
supervisor \  
openssh-server \  
net-tools tzdata language-pack-en-base \  
lsof initramfs-tools upstart-sysv \  
&& update-initramfs -u \  
&& apt-get purge systemd -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/log/supervisor /var/log/nginx /var/run/sshd /data/apps  
  
RUN useradd -ms /bin/bash david && usermod -aG sudo david  
RUN echo 'david:freego' | chpasswd  
RUN echo 'root:freego_2018' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile \  
&& echo "/var/www *(rw,async,no_subtree_check,insecure)" >> /etc/exports \  
&& echo "export TERM=xterm" >> ~/.bashrc  
ENV TZ=Asia/Chongqing  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN python -m pip install --upgrade --force pip  
RUN git clone https://github.com/torch/distro.git ~/torch --recursive  
RUN cd ~/torch && bash install-deps && ./install.sh && \  
cd install/bin && \  
./luarocks install nn && \  
./luarocks install dpnn && \  
./luarocks install image && \  
./luarocks install optim && \  
./luarocks install csvigo && \  
./luarocks install torchx && \  
./luarocks install tds  
  
RUN cd ~ && \  
mkdir -p ocv-tmp && \  
cd ocv-tmp && \  
curl -L https://github.com/Itseez/opencv/archive/2.4.11.zip -o ocv.zip && \  
unzip ocv.zip && \  
cd opencv-2.4.11 && \  
mkdir release && \  
cd release && \  
cmake -D CMAKE_BUILD_TYPE=RELEASE \  
-D CMAKE_INSTALL_PREFIX=/usr/local \   
-D BUILD_PYTHON_SUPPORT=ON \   
.. && \  
make -j8 && \  
make install && \  
rm -rf ~/ocv-tmp  
  
RUN cd ~ && \  
mkdir -p dlib-tmp && \  
cd dlib-tmp && \  
curl -L \  
https://github.com/davisking/dlib/archive/v19.0.tar.gz \  
-o dlib.tar.bz2 && \   
tar xf dlib.tar.bz2 && \  
cd dlib-19.0/python_examples && \  
mkdir build && \  
cd build && \  
cmake ../../tools/python && \  
cmake --build . --config Release && \  
cp dlib.so /usr/local/lib/python2.7/dist-packages && \  
rm -rf ~/dlib-tmp  
  
RUN cd ~ && git clone https://github.com/cmusatyalab/openface.git && \  
cd ~/openface && \  
./models/get-models.sh && \  
python setup.py install && \  
pip install numpy scipy pandas scikit-learn nose nolearn autobahn \  
imagehash twisted protobuf appdirs pyOpenSSL cryptography service-identity
matplotlib \  
flask flask_socketio  
  
# WORKDIR /root/openface  
WORKDIR /data/apps  
EXPOSE 22 1979  
ADD ./svr/ /data/apps  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]

