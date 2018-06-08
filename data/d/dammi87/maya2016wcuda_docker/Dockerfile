FROM nvidia/cuda:8.0-cudnn5-runtime-centos6  
  
RUN yum update -y && yum install -y \  
nano \  
csh \  
libXp \  
libXmu \  
libXpm \  
libXi \  
libtiff \  
libXinerama \  
elfutils \  
gcc \  
gstreamer-plugins-base.x86_64 \  
gamin \  
git \  
mesa-utils \  
mesa-libGL-devel \  
tcsh \  
xorg-x11-server-Xorg \  
xorg-x11-server-Xvfb \  
wget && \  
yum groupinstall -y "X Window System" && \  
yum clean all  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install \--target=/usr/local/lib/python2.6/site-packages \  
nose \  
mock \  
unittest2  
  
# Enable playblasts with Quicktime  
ENV LIBQUICKTIME_PLUGIN_DIR=/usr/autodesk/maya/lib  
  
# Start Xvfb  
# Provide an in-memory X-session for parts of Maya that require a GUI  
# such as cmds.playblast()  
ENV DISPLAY :99  
  
# Run on user login, this has the limitation of being run  
# each time a user logs into the Docker image. Suggestions  
# are welcome to make this only run once at startup.  
RUN echo "# Start Xvfb" >> ~/.bashrc && \  
echo "Xvfb :99 -screen 0 1024x768x16 2>/dev/null &" >> ~/.bashrc && \  
echo "while ! ps aux | \grep -q '[0]:00 Xvfb :99 -screen 0 1024x768x16';" >>
~/.bashrc && \  
echo " do echo 'Waiting for Xvfb...'; sleep 1; done" >> ~/.bashrc  
  
# Expose Python libraries to Maya  
ENV PYTHONPATH=/usr/local/lib/python2.6/site-packages  
  
# Download and unpack distribution first, Docker's caching  
# mechanism will ensure that this only happens once.  
RUN wget
http://download.autodesk.com/us/support/files/maya_2016_service_pack_2/Autodesk_Maya_2016_SP2_EN_Linux_64bit.tgz
-O maya.tgz && \  
mkdir /maya && tar -xvf maya.tgz -C /maya && \  
rm maya.tgz && \  
rpm -Uvh /maya/Maya*.rpm && \  
rm -r /maya  
  
# Make mayapy the default Python  
RUN echo alias hpython="\"/usr/autodesk/maya/bin/mayapy\"" >> ~/.bashrc && \  
echo alias hpip="\"mayapy -m pip\"" >> ~/.bashrc  
  
# Setup environment  
ENV MAYA_LOCATION=/usr/autodesk/maya/  
ENV PATH=$MAYA_LOCATION/bin:$PATH  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && \  
mayapy get-pip.py  
RUN mayapy -m pip install \  
nose \  
mock  
  
# Cleanup  
WORKDIR /root  

