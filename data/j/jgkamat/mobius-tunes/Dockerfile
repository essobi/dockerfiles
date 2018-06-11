# You can change this to any version of ubuntu with little consequence  
FROM ubuntu:15.04  
MAINTAINER Jay Kamat github@jgkamat.33mail.com  
  
# This dockerimage will serve as a 'static' base for this DoCIF project  
# Setup apt to be happy with no console input  
ENV DEBIAN_FRONTEND noninteractive  
  
# Use UTF-8, fixes some hard to debug issues  
# This is not workin on cirlceci's current setup. Will reenable once its
working again  
# RUN locale-gen en_US.UTF-8  
# ENV LANG en_US.UTF-8  
# setup apt tools and other goodies we want  
RUN apt-get update --fix-missing && apt-get -y install python3-pip python3 git  
  
RUN apt-get update --fix-missing && apt-get -y install libav-tools
python3-numpy python3-scipy libavbin-dev libavbin0  
RUN pip3 install wave && pip3 install pydub && pip3 install pyglet  
  
RUN git clone https://github.com/MountainRange/mobius-tunes.git mobius  
WORKDIR mobius/src  
  
CMD ["python3 /root/mobius/src/mobius.py"]  

