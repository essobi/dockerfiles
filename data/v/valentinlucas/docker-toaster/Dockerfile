#  
# Yocto Toaster Dockerfile  
#  
# Pull base image.  
FROM dockerfile/python  
  
# Install Toaster.  
RUN \  
pip install django==1.6 && \  
pip install South==0.8.4 && \  
cd / && \  
git clone -b dizzy git://git.yoctoproject.org/poky.git  
  
# Expose ports.  
EXPOSE 8000  
# Start toaster  
CMD ["source poky/oe-init-build-env"]  
CMD ["source toaster start "]  

