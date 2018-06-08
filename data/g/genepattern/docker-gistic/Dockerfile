# copyright 2017-2018 Regents of the University of California and the Broad
Institute. All rights reserved.  
FROM ubuntu:14.04  
# Note: FROM java and FROM r-base work too but take much longer apt-get
updating  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install -y wget && \  
apt-get install --yes bc vim libxpm4 libXext6 libXt6 libXmu6 libXp6 zip unzip  
  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install build-essential --yes && \  
apt-get install python-dev groff --yes --force-yes && \  
apt-get install default-jre --yes --force-yes && \  
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
apt-get install software-properties-common --yes --force-yes && \  
add-apt-repository ppa:fkrull/deadsnakes-python2.7 --yes  
  
RUN apt-get update --yes --force-yes && \  
apt-get install python2.7 --yes --force-yes && \  
python get-pip.py  
  
RUN pip install awscli  
  
RUN mkdir /home/gistic  
WORKDIR /home/gistic  
  
RUN mkdir /home/gistic/MCRInstaller  
  
RUN cd /home/gistic/MCRInstaller && \  
wget
https://www.mathworks.com/supportfiles/downloads/R2014a/deployment_files/R2014a/installers/glnxa64/MCR_R2014a_glnxa64_installer.zip
&& \  
unzip MCR_R2014a_glnxa64_installer.zip  
  
RUN mkdir /build  
COPY Dockerfile /build/Dockerfile  
  
COPY runMatlab.sh /usr/local/bin/runMatlab.sh  
COPY runS3OnBatch.sh /usr/local/bin/runS3OnBatch.sh  
COPY runLocal.sh /usr/local/bin/runLocal.sh  
COPY run-with-env.sh /usr/local/bin/run-with-env.sh  
COPY matlab.conf /etc/ld.so.conf.d/matlab.conf  
  
RUN chmod a+x /usr/local/bin/runMatlab.sh && \  
cd MCRInstaller && \  
/home/gistic/MCRInstaller/install -mode silent -agreeToLicense yes  
COPY module/gp_gistic2_from_seg /usr/local/bin/gp_gistic2_from_seg  
  
CMD ["/bin/bash", "runMatlab.sh"]  
  

