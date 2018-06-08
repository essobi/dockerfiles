FROM schwarty/python-base  
  
MAINTAINER schwarty  
  
# Environment variables  
ENV TERM linux  
  
# Update repository  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y libxp6 libxpm4 libxmu6 libxt6  
RUN apt-get install -y bc  
RUN apt-get install -y unzip  
  
WORKDIR /  
  
RUN mkdir build  
WORKDIR build  
  
RUN git clone https://github.com/nipy/nibabel.git  
RUN git clone https://github.com/nipy/nipy.git  
RUN git clone https://github.com/nilearn/nilearn.git  
  
RUN echo "building..."  
  
WORKDIR /build/nibabel  
RUN python setup.py install  
  
WORKDIR /build/nipy  
RUN python setup.py install  
  
WORKDIR /build/nilearn  
RUN python setup.py install  
  
# Install SPM  
ENV SPM_DIR /build/spm12b/spm12b_mcr/spm12b  
ENV SPM_MCR /usr/local/bin/spm12b  
  
RUN wget
http://www.fil.ion.ucl.ac.uk/spm/download/restricted/utopia/spm12b_r6033.zip  
RUN wget
http://www.fil.ion.ucl.ac.uk/spm/download/restricted/utopia/MCR/glnxa64/MCRInstaller.bin  
  
ADD spm12b /usr/local/bin/  
  
RUN chmod 755 /usr/local/bin/spm12b  
RUN chmod 755 MCRInstaller.bin  
  
RUN unzip spm12b_r6033.zip  
  
RUN mv MCRInstaller.bin /usr/local/src/  
RUN mv spm12b_r6033 /usr/local/src/  
  
WORKDIR /usr/local/src  
  
RUN ./MCRInstaller.bin -P bean421.installLocation="mcr" -silent  
RUN spm12b quit  
  
# # Neurodebian  
# RUN wget -O- http://neuro.debian.net/lists/trusty.de-m.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list  
# RUN apt-key adv --recv-keys --keyserver pgp.mit.edu 2649A5A9  
# RUN apt-get update -y  
# RUN apt-get install -y fsl  
# # RUN source /etc/fsl/5.0/fsl.sh  
# # Cleanup  
# WORKDIR /  
# RUN rm -rf /build  
# RUN rm -rf /usr/local/src/spm8.tgz  
# RUN apt-get autoremove -y  
# RUN apt-get clean all

