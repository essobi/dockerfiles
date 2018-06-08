# \------------------------------------------------  
# packer-rancheros Dockerfile  
# \------------------------------------------------  
# Using Alpine Linux image to minimize the size of  
# the resulting image  
# \------------------------------------------------  
  
FROM alpine:latest  
MAINTAINER Joseph Callen <jcpowermac@gmail.com>  
  
# \------------------------------------------------  
# Environmental Variables  
# \------------------------------------------------  
# These define the paths for the projects  
# required files.  
# Using Filesystem Hierarchy Standard  
# http://www.pathname.com/fhs/  
# \------------------------------------------------  
  
ENV packer_bin_dir /opt/hashicorp/bin  
ENV packer_path ${packer_bin_dir}/packer  
  
# \------------------------------------------------  
# Run - Packages  
# \------------------------------------------------  
# Update package list  
# Install qemu, qemu-img, wget, unzip,  
# Python Requests, Python Pip  
# Common OVF Tool (cot)  
# \------------------------------------------------  
  
RUN apk update && \  
apk add qemu-system-x86_64 qemu-img wget unzip py-requests py-pip && \  
pip install cot  
  
# \------------------------------------------------  
# Run - Download and Install Packer  
# \------------------------------------------------  
# Create directory for packer  
# Use the GitHub API to get the latest tag  
# Requests. Download packer to /tmp  
# Unzip into the ./bin/ directory  
# \------------------------------------------------  
  
RUN mkdir -p ${packer_bin_dir} \  
&& cd ${packer_bin_dir} \  
&& wget -nv $(python -c 'import requests;version =
requests.get("https://api.github.com/repos/mitchellh/packer/tags").json()[0]["name"].replace("v","");print
"https://releases.hashicorp.com/packer/%s/packer_%s_linux_amd64.zip" %
(version,version)') -O /tmp/packer.zip \  
&& unzip /tmp/packer.zip -d ${packer_bin_dir}  
  
# \------------------------------------------------  
# Copy  
# \------------------------------------------------  
# 1\. Copy the configuration files and ovf to  
# build image with Packer  
# 2\. Copy the docker-entrypoint Python script  
# to /  
# \------------------------------------------------  
  
COPY cloud-config.yml minimal.ovf rancheros.json /opt/hashicorp/etc/packer/  
COPY docker-entrypoint.py /  
  
  
# \------------------------------------------------  
# Volumes  
# \------------------------------------------------  
# Create a volume on /build. Packer will use this  
# location as output for the resulting image.  
# \------------------------------------------------  
VOLUME /build  
  
# \------------------------------------------------  
# Workdir  
# \------------------------------------------------  
# Change directory to build directory  
# \------------------------------------------------  
WORKDIR /build  
  
# \------------------------------------------------  
# Entrypoint  
# \------------------------------------------------  
# docker-entrypoint.py determines the latest  
# version of RancherOS via the GitHub API.  
# Appends the Packer -var option to include the  
# iso_url and the checksum if build is in the  
# argument list.  
# \------------------------------------------------  
ENTRYPOINT ["/docker-entrypoint.py"]  
CMD ["--help"]  
EXPOSE 5910 5911  
  

