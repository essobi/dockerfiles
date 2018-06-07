FROM centos:7  
MAINTAINER "Stefan Walraven" <stefan.walraven@cs.kuleuven.be>  
  
ENV FRICTION_VERSION 2K6  
  
RUN yum updateinfo && yum install -y \  
sed \  
fortran \  
gfortran \  
gcc-gfortran \  
wget  
  
RUN wget -q http://www.dept.aoe.vt.edu/~mason/Mason_f/friction2k6.f  
RUN wget -q http://www.dept.aoe.vt.edu/~mason/Mason_f/F15frict.inp  
  
RUN sed -i 's_ USE DFPORT_C USE DFPORT_g' friction2k6.f  
RUN sed -i "s_Pause 'Press the ENTER key to exit'_WRITE(*,*) 'Press the ENTER
key to exit' \n READ(*,*) _g" friction2k6.f  
RUN sed -i "s_Pause 'Press ENTER key to terminate'_WRITE(*,*) 'Press the ENTER
key to exit' \n READ(*,*) _g" friction2k6.f  
  
RUN gfortran -o friction2k6 friction2k6.f  
RUN cp friction2k6 /usr/bin/  
  
# CMD ["./friction2k6", "F15frict.inp", "F15frict.out"]  
CMD ["/bin/bash"]  

