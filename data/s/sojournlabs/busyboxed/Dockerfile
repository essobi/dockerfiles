# Run a file packaged by sojournlabs/busyboxer.  
# Usage:  
# docker run -t -i --rm -v /path/to/program/:/vapr/build:ro
sojournlabs/busyboxed program arguments  
#  
FROM busybox  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
ADD busyboxed /bin/busyboxed  
VOLUME ["/vapr/build"]  
ENTRYPOINT ["/bin/busyboxed"]  

