FROM ubuntu:14.04  
RUN apt-get update -y  
RUN apt-get install -y build-essential git  
RUN apt-get install -y qt4-qmake libqt4-dev libqt4-sql-sqlite  
RUN apt-get install -y gcovr lcov  
RUN apt-get install -y doxygen graphviz mscgen  
RUN apt-get install -y xinetd vnc4server xvfb blackbox x11-apps x11-utils  
RUN apt-get install -y dbus-x11  
RUN apt-get install -y clang-3.6 clang-format-3.6 git  
RUN apt-get install -y python-minimal python-tornado python-gevent python-yaml  
RUN apt-get install -y ccache  
RUN mkdir -p /var/run/dbus  
RUN echo "QMAKE_CXX = ccache g++" >>
/usr/share/qt4/mkspecs/linux-g++-64/qmake.conf  
  
ENV DISPLAY :10  
COPY runserver.sh /bin  
  
CMD [ "/bin/runserver.sh" ]  

