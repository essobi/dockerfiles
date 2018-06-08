# Taking hemelb as base image  
FROM hemelb-joslin  
MAINTAINER Miguel O. Bernabeu (miguel.bernabeu@ed.ac.uk)  
  
##  
# Dependencies  
##  
RUN apt-get update && apt-get install -y \  
qhull-bin \  
unzip \  
wget \  
libfreetype6-dev \  
pkg-config \  
python-tk \  
libgeos-dev \  
&& rm -rf /var/lib/apt/lists/*  
RUN pip install matplotlib pandas openpyxl shapely descartes  
  
##  
# Download and install MATLAB's MCR  
##  
WORKDIR /opt  
RUN wget
https://uk.mathworks.com/supportfiles/downloads/R2017a/deployment_files/R2017a/installers/glnxa64/MCR_R2017a_glnxa64_installer.zip
&& \  
unzip MCR_R2017a_glnxa64_installer.zip && \  
mkdir /opt/mcr && \  
./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \  
rm MCR_R2017a_glnxa64_installer.zip  
  
##  
# MCR installs its own linux runtime libraries and uses $LD_LIBRARY_PATH to
give them priority over system ones.  
# There are versioning issues between them and the ones provided by Ubuntu
which were used to compile various PolNet components.  
# Copy VMTK libraries to a visible location.  
##  
RUN mv /opt/mcr/v92/sys/os/glnxa64/libstdc++.so.6
/opt/mcr/v92/sys/os/glnxa64/libstdc++.so.6.bak && \  
mv /opt/mcr/v92/bin/glnxa64/libexpat.so.1
/opt/mcr/v92/bin/glnxa64/libexpat.so.1.bak  
RUN cp $VMTKHOME/lib/lib* /usr/lib/x86_64-linux-gnu/  
  
##  
# Download and install the standalone version of PolNet  
##  
WORKDIR /tmp  
RUN wget https://www.dropbox.com/s/s6lkhhmdokjgyx7/PolNet_files.zip?dl=0 && \  
mv PolNet_files.zip?dl=0 PolNet_files.zip && \  
unzip PolNet_files.zip && \  
cp PolNet_files/* /usr/local/bin/ && \  
chmod +x /usr/local/bin/PolNet /usr/local/bin/run_PolNet.sh && \  
rm -rf PolNet_files*  
  
##  
# Place a PolNet launcher and a symlink to the data directory on the Desktop
of the root user home space  
##  
COPY polnet.desktop /root/Desktop/  
RUN ln -s /data /root/Desktop/  
  
##  
# Copy the ROI analysing script somewhere that Python can find  
##  
COPY ExtractResultsFromROI.py /usr/local/bin/ExtractResultsFromROI  
RUN chmod +x /usr/local/bin/ExtractResultsFromROI  
COPY ComputeMAFlowDrop.py /usr/local/bin/ComputeMAFlowDrop  
RUN chmod +x /usr/local/bin/ComputeMAFlowDrop  
COPY ComputeMorphologicalIndices.py /usr/local/bin/ComputeMorphologicalIndices  
RUN chmod +x /usr/local/bin/ComputeMorphologicalIndices  
COPY ComputeMAFlowDropPerRegions.py /usr/local/bin/ComputeMAFlowDropPerRegions  
RUN chmod +x /usr/local/bin/ComputeMAFlowDropPerRegions  
  
##  
# Download and place the example data distributed with the protocol paper in a
Desktop subdirectory of the root user home space  
##  
WORKDIR /tmp  
RUN wget
https://www.dropbox.com/s/nc8l6xig26jbw0a/990_Example2-skeleton.tif?dl=0
https://www.dropbox.com/s/n0pforgr7r7dc9p/990_Example2-flat.tif?dl=0 && \  
mv 990_Example2-skeleton.tif?dl=0 990_Example2-skeleton.tif && \  
mv 990_Example2-flat.tif?dl=0 990_Example2-flat.tif && \  
mkdir /root/Desktop/paper_example_data/ && \  
mv 990_Example2* /root/Desktop/paper_example_data/ && \  
echo "Any intermediate file saved to this directory will disappear every time
that the container is stopped and restarted. Copy the example data to /data
(which maps to a directory in the host machine) in order for the intermediate
files to persist." > /root/Desktop/paper_example_data/README.txt  

