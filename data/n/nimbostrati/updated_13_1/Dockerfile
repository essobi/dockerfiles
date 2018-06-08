FROM nimbostrati/opensuse_13_1_base  
MAINTAINER Stephen Moore, stephen.moore@linux.com  
  
RUN zypper --non-interactive addrepo --no-gpgcheck
http://download.opensuse.org/update/13.1/ openSUSE-13.1-Update  
RUN zypper --non-interactive update  
  
ENTRYPOINT ["/bin/bash", "-c", "uname -a"]  
  

