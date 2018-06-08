# Base Image: CentOS 7 - https://hub.docker.com/_/centos  
#  
# CentOS images with a major version number are rolling builds, for example
centos:6 or centos:7.  
# These images will be updated monthly or as needed for emergency fixes.  
# Therefore a build based on a major-tagged CentOS base image does not produce
the same environment with every build.  
#  
# Images with minor version tags DO NOT recieve updates as they are intended
to  
# match installation iso contents, for example centos:7.1.1503 or centos:6.7.  
# If a minor-tagged image is used, when including "yum -y update" or "yum -y
install <something>" in the Dockerfile,  
# the system also updates with the latest packages and so the final image
might also differs every time.  
#  
# When triggered, this Dockerfile always uses the latest CentOS 7 base image
and updates.  
FROM centos:7  
# Set default timezone.  
# An alternative way to set timezone is to run container with: -e
"TZ=Continent/City".  
ENV TZ America/Los_Angeles  
  
# When a package is downloaded, installed and removed there is a chance that  
# the package may still be saved/stored in the yum's cache. So to clean all
the  
# cached packages run "yum clean all" at the end of an image building.  
RUN yum -y install epel-release \  
&& yum -y update \  
&& yum clean all  
  
# Entrypoint Executable  
# To override the entrypoint, run docker with "--entrypoint=<something else>".  
ENTRYPOINT ["/bin/bash"]  
  
# Entrypoint Options  
CMD [""]  

