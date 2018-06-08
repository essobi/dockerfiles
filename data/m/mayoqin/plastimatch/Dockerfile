# Build a CentOS based system  
FROM mayoqin/gruntubuntu  
LABEL maintainer "Panagiotis Korfiatis korfiatis.panagiotis@mayo.edu"  
  
RUN apt-get -y update && apt-get install -y \  
wget \  
unzip \  
build-essential \  
xutils-dev \  
default-jre \  
python-pip \  
cmake  
  
RUN pip install wget  
RUN pip install requests  
WORKDIR /  
  
# DCMTK (Offis DICOM Toolkit)  
# http://dcmtk.org/dcmtk.php.en  
RUN apt-get install -y dcmtk  
RUN apt-get install -y plastimatch  
  
# change to top level directory  
WORKDIR /  
  
# cleanup  
RUN apt-get purge -y build-essential xutils-dev  
RUN apt-get clean autoclean  
RUN apt-get autoremove -y  
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Copy code and configuration files  
COPY niitodicom.py ./  
COPY dicomtonii.py ./  
RUN chmod +x dicomtonii.py  
RUN chmod +x niitodicom.py  
COPY plastimatch.yml /grunt.d/gruntfile.yml  
# What do we run on startup?  
CMD ["/bin/grunt", "/grunt.d/gruntfile.yml"]  
# We expose port 9901 by default  
EXPOSE 9901:9901  

