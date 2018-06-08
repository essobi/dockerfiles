# Package a binary file and all its dependencies into /vapr/build.  
# Usage:  
# docker run -t -i --rm -v `pwd`:/vapr/build sojournlabs/busyboxer command
[from_package]  
# Then untar the resultant .tar.gz file into a busybox Docker image's root.  
FROM debian  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
ADD busyboxer /bin/busyboxer  
VOLUME ["/vapr/build"]  
ENTRYPOINT ["/bin/busyboxer"]  

