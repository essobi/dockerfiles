FROM fedora:latest  
MAINTAINER https://github.com/SatelliteQE  
  
RUN dnf -y update; dnf clean all  
RUN dnf groupinstall -y "Development Tools"  
RUN dnf install -y redhat-rpm-config-36 python-devel gcc gcc-c++ make flex \  
bison gperf ruby openssl-devel freetype-devel fontconfig-devel libicu-devel \  
sqlite-devel libpng-devel libjpeg-devel libxslt-devel libxml2-devel which \  
git python-pip  
  
# Upgrade pip itself  
RUN pip install --upgrade pip; easy_install Cython  
  
ENV HOME /root  
WORKDIR /root  
  
# Clone Robottelo  
RUN git clone https://github.com/SatelliteQE/robottelo.git  
  
# Install Python deps  
RUN cd /root/robottelo && pip install -r requirements.txt && \  
pip install -r requirements-optional.txt  
  
# Clone Automation-tools  
RUN git clone https://github.com/SatelliteQE/automation-tools.git  
  
# Install Python deps  
RUN cd /root/automation-tools && pip install -r requirements.txt  
  
# Add phantomjs  
RUN git clone git://github.com/ariya/phantomjs.git  
RUN cd /root/phantomjs && git checkout 2.0  
RUN cd /root/phantomjs && ./build.sh --confirm --silent --jobs 2  
  
# Move the binary  
RUN cp /root/phantomjs/bin/phantomjs /usr/bin/.  
  
# Clean up  
RUN rm -rf /root/phantomjs  
  
# runtime  
EXPOSE 22

