#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM qqdsfmt/webrtc_checkout  
  
ADD root/depot_tools.sh /root/depot_tools.sh  
  
RUN \  
/root/depot_tools.sh  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

