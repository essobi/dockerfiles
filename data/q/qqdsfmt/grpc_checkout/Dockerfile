#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM qqdsfmt/webrtc_checkout  
  
ADD root/checkout.sh /root/checkout.sh  
  
RUN \  
/root/checkout.sh  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

