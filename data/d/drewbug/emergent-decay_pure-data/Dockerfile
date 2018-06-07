# BUILD-USING: docker build -t drewbug/emergent-decay_pure-data .  
# RUN-USING: docker run -name pure-data drewbug/emergent-decay_pure-data &&
docker wait pure-data && docker cp pure-data:/pd-
extended/packages/linux_make/build/Pd-0.43.4-extended.tar.bz2 . && docker rm
pure-data  
FROM centos  
MAINTAINER Drew Carey Buglione <me@drewb.ug>  
  
RUN yum groupinstall -y "Development Tools"  
  
RUN wget
http://sourceforge.net/projects/lame/files/lame/3.99/lame-3.99.5.tar.gz/download
&& \  
tar xvfz lame-3.99.5.tar.gz && \  
cd lame-3.99.5 && ./configure && make && make install && ldconfig && cd .. &&
\  
rm -r lame-3.99.5 lame-3.99.5.tar.gz  
  
RUN yum install -y fftw3-devel lua-devel tcl-devel libvorbis-devel ladspa-
devel speex-devel mesa-libGL-devel mesa-libGLU-devel gsl-devel  
  
RUN wget http://sourceforge.net/projects/pure-data/files/pd-
extended/0.43.4/Pd-extended_0.43.4-source.tar.bz2/download && \  
tar xvfj Pd-extended_0.43.4-source.tar.bz2 && \  
rm Pd-extended_0.43.4-source.tar.bz2  
RUN sed 's/lua5/lua-5/' -i /pd-extended/externals/loaders/pdlua/src/Makefile  
  
WORKDIR pd-extended/packages/linux_make  
CMD make PACKAGE_TYPE=tarbz2 install && make PACKAGE_TYPE=tarbz2 package  

