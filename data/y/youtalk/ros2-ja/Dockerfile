FROM youtalk/ubuntu-ja:xenial  
MAINTAINER Yutaka Kondo <yutaka.kondo@youtalk.jp>  
  
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" >
/etc/apt/sources.list.d/ros-latest.list'  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
421C365BD9FF1F717815A3895523BAEEB01FA116  
  
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu xenial
main" > /etc/apt/sources.list.d/gazebo-latest.list'  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
D2486D2DD83DB69272AFE98867170598AF249743  
  
RUN apt-get update && apt-get -q -y install \  
git wget build-essential cppcheck cmake \  
libopencv-dev libpoco-dev libpocofoundation9v5 libpocofoundation9v5-dbg \  
python-empy python3-dev python3-empy python3-nose python3-pip
python3-setuptools python3-vcstool \  
libtinyxml-dev libeigen3-dev clang-format \  
pydocstyle pyflakes python3-coverage python3-mock python3-pep8 \  
uncrustify libasio-dev libtinyxml2-dev \  
libboost-chrono-dev libboost-date-time-dev libboost-program-options-dev
libboost-regex-dev libboost-system-dev libboost-thread-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip3 install flake8 flake8-import-order  
  
RUN mkdir -p /root/ros2_ws/src  
WORKDIR /root/ros2_ws  
RUN wget https://raw.githubusercontent.com/ros2/ros2/release-latest/ros2.repos  
RUN vcs import src < ros2.repos  
  
RUN src/ament/ament_tools/scripts/ament.py build --build-tests --symlink-
install --isolated  
  
COPY ./ros2_entrypoint.sh /  
  
ENTRYPOINT ["/ros2_entrypoint.sh"]  
CMD ["bash"]  

