# http://wiki.paparazziuav.org/wiki/Installation  
FROM ubuntu:latest  
  
ADD deps.sh .  
  
RUN bash deps.sh  
  
# Workaround for invalidating cache if branch-head changes.  
# https://stackoverflow.com/questions/36996046/how-to-prevent-dockerfile-
caching-git-clone  
ADD https://api.github.com/repos/paparazzi/paparazzi/git/refs/heads/$branch \  
version.json  
RUN git clone https://github.com/paparazzi/paparazzi.git  
  
WORKDIR paparazzi  
  
ARG paparazzi_tag=v5.12_stable  
  
RUN git checkout tags/$paparazzi_tag \  
&& make  
  
# cp conf/system/udev/rules/*.rules /etc/udev/rules.d/  
# udevadm control --reload-rules  
ENTRYPOINT [ "./paparazzi" ]  

