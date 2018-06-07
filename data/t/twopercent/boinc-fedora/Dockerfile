FROM fedora:latest  
MAINTAINER "Chris Moser" chrismmoser@gmail.com  
RUN dnf -y upgrade && dnf install -y boinc-client && dnf clean all  
USER boinc  
CMD "/bin/bash"  
EXPOSE 31416/tcp 443/tcp 80/tcp  
WORKDIR /var/lib/boinc  
ENTRYPOINT /usr/bin/boinc_client --allow_multiple_clients --attach_project
http://einstein.phys.uwm.edu 485723_20d7cf0683d453b3fac3f85185b401f3  
#ENTRYPOINT /bin/bash  

