# Use Ubuntu 14.04 as a base image  
FROM ubuntu:14.04  
  
RUN apt-get update && \  
apt-get install -y \  
python2.7-minimal \  
bash-completion \  
wget \  
mesa-utils \  
binutils \  
module-init-tools \  
iputils-ping \  
net-tools \  
libxmu6 \  
libglu1-mesa \  
libfreetype6 \  
libgl2ps0 \  
libfreeimage3 \  
libicu52 \  
libglib2.0-0 \  
libgfortran3 && \  
# Perform cleanup \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/python2.7 /usr/bin/python  
  
# Copy the current directory contents into the container at /app  
  
RUN wget -O SALOME-8.3.0-UB14.04.tgz "http://www.salome-
platform.org/downloads/current-
version/DownloadDistr?platform=UB14.04&version=8.3.0" && \  
tar -zxf SALOME-8.3.0-UB14.04.tgz && \  
rm SALOME-8.3.0-UB14.04.tgz && \  
mv SALOME-8.3.0-UB14.04 /opt/SALOME-8.3.0-UB14.04  
# Define environment variable  
ENV PATH="/opt/SALOME-8.3.0-UB14.04/:${PATH}"  
  
RUN useradd -ms /bin/bash saluser  
  
# Define environment variable  
ENV PATH="/opt/SALOME-8.3.0-UB14.04/:${PATH}"  
  
USER saluser  
  
CMD ["bash"]  

