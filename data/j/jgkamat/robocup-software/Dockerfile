# Use phusion/baseimage if problems arise  
FROM robojackets/robocup-baseimage:master  
MAINTAINER Jay Kamat github@jgkamat.33mail.com  
  
WORKDIR /home/developer  
RUN git clone https://github.com/RoboJackets/robocup-software.git  
WORKDIR /home/developer/robocup-software  
  
# Build  
RUN git submodule update --init  
RUN make  
  
# to run X11 Server  
# docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix
<COMMAND NAME>  
CMD [ "-c", "make run-sim" ]  

