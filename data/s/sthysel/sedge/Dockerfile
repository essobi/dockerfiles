FROM python:3-onbuild  
MAINTAINER sthysel <sthysel@gmail.com>  
ENV REFRESHED_AT 2015-03-06  
# ssh keys, usually found in ~/.ssh/  
# map it to /keys in the container  
VOLUME /keys  
  
ENV HELPSTR "Map ~/.ssh to /keys: -v ${HOME}/.ssh:/keys"  
COPY sedgerunner.sh /  
  
ENTRYPOINT ["/sedgerunner.sh"]  
CMD ["/usr/local/bin/sedge"]  

