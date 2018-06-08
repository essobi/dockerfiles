FROM ubuntu:16.04  
MAINTAINER "Victor Maus" maus@iiasa.ac.at  
  
# Set GAMS version  
ENV LATEST=24.8.5  
ENV GAMS_VERSION=24.5.6  
  
# Set GAMS bit architecture, either 'x64_64' or 'x86_32'  
ENV GAMS_BIT_ARC=x64_64  
  
# Install wget  
RUN apt-get update && apt-get install -y --no-install-recommends wget curl
software-properties-common git  
  
# Download GAMS  
RUN curl -SL
"https://d37drm4t2jghv5.cloudfront.net/distributions/${GAMS_VERSION}/linux/linux_${GAMS_BIT_ARC}_sfx.exe"
\--create-dirs -o /opt/gams/gams.exe  
  
# Install GAMS  
RUN cd /opt/gams &&\  
chmod +x gams.exe; sync &&\  
./gams.exe &&\  
rm -rf gams.exe  
  
# Configure GAMS  
RUN GAMS_PATH=$(dirname $(find / -name gams -type f -executable -print)) &&\  
echo "export PATH=\$PATH:$GAMS_PATH" >> ~/.bashrc &&\  
cd $GAMS_PATH &&\  
./gamsinst -a  
  

