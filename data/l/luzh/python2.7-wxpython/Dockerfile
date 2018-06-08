# Python 2.7 with wxPython  
#  
# --- Image Stack ---  
# luzh/python2.7-wxpython  
# luzh/python2.7-imaging  
# luzh/python2.7-numerical  
# luzh/python2.7-baseline  
# luzh/centos7  
  
FROM luzh/python2.7-imaging  
  
# Refer to https://github.com/wxWidgets/Phoenix for wxPython-Phoenix
dependencies.  
# This Dockerfile builds wxPython NOT wxPython-Phoenix because the pip install  
# method provided by the wxPython-Phoenix website gives errors in the end.  
# pip install --no-cache-dir --upgrade --trusted-host wxpython.org --pre -f
http://wxpython.org/Phoenix/snapshot-builds/ wxPython_Phoenix  
# Set the Python version to be built and installed.  
  
ENV WXPYTHON_VERSION 3.0.2.0  
# The installed path should be /usr/local.  
  
RUN yum -y install dpkg dpkg-devel \  
&& yum -y install SDL SDL-devel \  
&& yum -y install webkitgtk webkitgtk-devel \  
&& yum -y install gtk+ gtk+-devel \  
&& yum -y install gtk2 gtk2-devel \  
&& yum -y install wxGTK wxGTK-devel \  
&& yum -y install wxGTK3 wxGTK3-devel \  
&& yum -y install libnotify libnotify-devel \  
&& yum -y install freeglut freeglut-devel \  
&& yum -y install gstreamer gstreamer-devel \  
&& yum -y install gstreamer-python gstreamer-python-devel \  
&& yum -y install gstreamer-plugins-base gstreamer-plugins-base-devel \  
&& mkdir /build && cd /build \  
&& curl -SL
"http://sourceforge.net/projects/wxpython/files/wxPython/$WXPYTHON_VERSION/wxPython-
src-$WXPYTHON_VERSION.tar.bz2" -o wxPython.tar.bz2 \  
&& mkdir /build/wxPython \  
&& tar -jxvf wxPython.tar.bz2 --strip-components=1 -C /build/wxPython \  
&& cd /build/wxPython/wxPython \  
&& python2.7 ./build-wxpython.py --build_dir=../wxBuild \  
&& python2.7 ./build-wxpython.py --install --build_dir=../wxBuild \  
&& cd && rm -rf /build \  
&& yum clean all  

