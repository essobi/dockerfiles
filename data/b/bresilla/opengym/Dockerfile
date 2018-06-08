FROM nvidia/cuda:9.0-cudnn7-devel  
LABEL maintainer="bresilla <trim.bresilla@gmail.com>"  
WORKDIR /  
  
# 1. installing python2 and python3  
RUN apt-get update && \  
apt install -y --no-install-recommends python python3 python-pip python3-pip
python-setuptools python3-setuptools python-tk python3-tk  
# 1.1 uppgrade pip and pip3  
RUN pip3 install --upgrade pip setuptools && pip install --upgrade pip
setuptools  
  
# 2. installing jupyter, and a bunch of Science Python Packages  
RUN pip3 install jupyter pandas matplotlib scipy seaborn setuptools scikit-
learn scikit-Image sympy cython patsy statsmodels cloudpickle dill numba bokeh  
  
# 3. installing Tensorflow (GPU)  
RUN pip3 install tensorflow-gpu  
RUN pip3 install
http://download.pytorch.org/whl/cu90/torch-0.4.0-cp35-cp35m-linux_x86_64.whl
torchvision  
RUN pip3 install chainer cupy-cuda90  
RUN pip3 install keras  
  
# 4. installing OpenAI Gym (plus dependencies)  
RUN pip3 install gym pyopengl pyvirtualdisplay  
# 4.1 installing roboschool and its dependencies. We love FOSS  
RUN apt-get install -y --no-install-recommends cmake ffmpeg pkg-config
qtbase5-dev libqt5opengl5-dev libassimp-dev libpython3.5-dev libboost-python-
dev libtinyxml-dev  
# This got some dependencies, so let's get going  
WORKDIR /gym  
ENV ROBOSCHOOL_PATH="/gym/roboschool"  
# installing bullet (the physics engine of roboschool) and its dependencies  
RUN apt-get install -y --no-install-recommends git gcc g++ && \  
git clone https://github.com/openai/roboschool && \  
git clone https://github.com/olegklimov/bullet3 -b roboschool_self_collision
&& \  
mkdir bullet3/build && \  
cd bullet3/build && \  
cmake -DBUILD_SHARED_LIBS=ON -DUSE_DOUBLE_PRECISION=1
-DCMAKE_INSTALL_PREFIX:PATH=$ROBOSCHOOL_PATH/roboschool/cpp-
household/bullet_local_install -DBUILD_CPU_DEMOS=OFF -DBUILD_BULLET2_DEMOS=OFF
-DBUILD_EXTRAS=OFF -DBUILD_UNIT_TESTS=OFF -DBUILD_CLSOCKET=OFF
-DBUILD_ENET=OFF -DBUILD_OPENGL3_DEMOS=OFF .. && \  
make -j4 && \  
make install  
  
WORKDIR /gym/roboschool  
RUN pip3 install -e ./  
  
# 5. installing X and xvfb so we can SEE the action using a remote desktop
access (VNC) and cleanup  
RUN pip3 install tqdm gym[atari]  
RUN apt-get install -y x11vnc xvfb fluxbox wmctrl fish tmux ranger x11-apps
firefox && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
# VNC Server  
EXPOSE 5900  
WORKDIR /  
  
RUN useradd -ms /bin/bash bresilla  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/bresilla && \  
echo "bresilla:x:${uid}:${gid}:bresilla,,,:/home/bresilla:/bin/bash" >>
/etc/passwd && \  
echo "bresilla:x:${uid}:" >> /etc/group && \  
echo "bresilla ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/bresilla && \  
chmod 0440 /etc/sudoers.d/bresilla && \  
chown ${uid}:${gid} -R /home/bresilla  
  
COPY x11vnc /

