FROM ucuapps/robert:latest  
  
MAINTAINER "UCU APPS"  
LABEL Description="This ROS Kinetic image for Robert development with IDEs for
NVidia Graphic Card" Vendor="UCU APPS" Version="1.0"  
  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
ENV PATH /usr/local/nvidia/bin:${PATH}  
  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["/usr/bin/terminator"]

