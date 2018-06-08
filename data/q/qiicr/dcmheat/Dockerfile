#FROM thewtex/centos-build:latest  
#FROM fedorov/docker-centos-build:centos7  
FROM centosbuild/centos7:latest  
  
#FROM stevepieper/slicer  
#RUN apt-get update  
#RUN apt-get install --yes curl zip unzip  
ADD setup_slicer.sh /usr/src/setup_slicer.sh  
RUN /usr/src/setup_slicer.sh  
  
RUN rpm --import https://winswitch.org/gpg.asc && \  
cd /etc/yum.repos.d/ && \  
wget https://winswitch.org/downloads/CentOS/winswitch.repo && \  
yum -y install xpra  
  
#ADD setup_dcm2niix.sh /usr/src/setup_dcm2niix.sh  
#RUN /usr/src/setup_dcm2niix.sh  
## Setup tools  
### dcm2niix - build from source, since binaries have issues with missing
GLIBC version  
### installs to /usr/local, in the PATH  
RUN yum install -y libstdc++-static  
RUN cd /tmp && \  
git clone https://github.com/rordenlab/dcm2niix.git && \  
cd dcm2niix && git checkout v1.0.20171215 && \  
mkdir build && cd build && \  
cmake -DBATCH_VERSION=ON -DCMAKE_INSTALL_PREFIX=/usr -DUSE_OPENJPEG=ON .. && \  
make && make install  
  
### plastimatch  
RUN cd /tmp && \  
git clone https://gitlab.com/plastimatch/plastimatch.git && \  
cd plastimatch && git checkout v1.7.2 && \  
mkdir build && cd build && \  
cmake -DINSTALL_PREFIX=/usr .. && \  
make && make install && \  
cp plastimatch /usr/bin  
  
### FreeSurfer  
### This one is 4.5Gb!  
#RUN curl -c -v -L
ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-
centos6_x86_64-stable-pub-v6.0.0.tar.gz | tar xz -C /usr/  
#ENV PATH="/usr/dcm2niix:${PATH}"  
### python tools  
ADD get-pip.py /usr/src/get-pip.py  
RUN python /usr/src/get-pip.py && pip install nibabel  
  
### This is needed to run Slicer python scripts in a headless mode  
RUN xpra --xvfb="Xorg +extension GLX -config /etc/xpra/xorg.conf -logfile
${HOME}/.xpra/xorg.log" start :9  
ENV DISPLAY :9  
## Get the cmake test setup  
ADD test /usr/src/test  
RUN mkdir /usr/dcmheat && cd /usr/dcmheat && cmake /usr/src/test  
  
# Didn't figure this one out - will start xpra in the runner script  
#RUN pip install supervisor  
#RUN mkdir -p /etc/supervisord/conf.d  
#ADD supervisord.conf /etc/supervisord/supervisord.conf  
#ADD supervisord.service /usr/lib/systemd/system/supervisord.service  
#RUN mkdir -p /var/log/supervisor  
#RUN systemctl enable supervisord  
ADD etc/X11 /etc/X11  
  
RUN mkdir -p /src/.config/www.na-mic.org && mkdir /src/SlicerDB  
ADD Slicer.ini /src/.config/www.na-mic.org  
  
ENV PATH "/usr/slicer:${PATH}"  
ADD tester.py /src  
RUN yum install -y tree  
RUN pip install dicom2nifti==1.2.21  
  
## Setup data  
RUN mkdir /usr/data  
ADD setup_datasets.sh /usr/src/setup_datasets.sh  
RUN /usr/src/setup_datasets.sh  
ADD SlicerConvert.py /usr/src/SlicerConvert.py  

