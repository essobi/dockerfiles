# ftp://ftp.kddlabs.co.jp/lang/tcl/ftp.scriptics.com/tcl_old/tcl7.3.tar.Z  
# ftp://ftp.kddlabs.co.jp/lang/tcl/ftp.scriptics.com/tcl_old/tk3.6.tar.Z  
# http://stackoverflow.com/a/25334301/2352259  
# http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/  
FROM aidanhs/centos:2.1  
ENV HOME /root  
WORKDIR /root  
ADD tclrpms tkrpms /root/rpms/  
RUN rpm -i --ignorearch /root/rpms/*  
# tcl  
ADD tcl7.3.tar.gz tk3.6.tar.gz /root/  
RUN cd tcl7.3 && \  
cp tclUnixStr.c tclUnixStr.c.bak && \  
sed 's|^\\(.*case EDEADLK.*\\)$|//\1|' tclUnixStr.c.bak > tclUnixStr.c  
RUN cd tcl7.3 && ./configure && make && make install  
# tk  
RUN cd /usr && ln -s X11R6 X11R5  
RUN cd tk3.6 && ./configure && make && make install  
CMD /bin/bash  
  
# To make tk work:  
# - xhost + && docker run -e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix:ro -i
-t aidanhs/tcl:7.3 && xhost -  
#  
# `xhost +` should NOT be used on multi-user environments (look at the SO
question at the top).  

