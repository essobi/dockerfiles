FROM ubuntu:14.04  
LABEL maintainer="Michael Wess <michael.wess@boku.ac.at>"  
  
RUN apt-get update -y && \  
apt-get install -y software-properties-common --no-install-recommends && \  
apt-add-repository -y ppa:ubuntugis/ubuntugis-unstable &&\  
apt-get -y update &&\  
apt-get install -qqy otb-bin otb-bin-qt python-otb --no-install-recommends &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home/data  
  
ENTRYPOINT  
CMD ["/bin/bash"]  

