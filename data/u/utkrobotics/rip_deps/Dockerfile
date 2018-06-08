FROM robobenklein/home:latest  
# $LUSER is user with 901:901 from home image  
# deps for rip build  
RUN sudo install_clean \  
cmake g++ git curl xz-utils fakeroot automake \  
doxygen lcov \  
libssh2-1-dev libssl-dev \  
libqt5opengl5-dev \  
libeigen3-dev libsuitesparse-dev  
  
# Create a new robot user:  
USER root  
ENV RUSER=dogcow  
RUN groupadd -r ${RUSER} -g 902  
RUN useradd -m -u 902 -r -g 902 ${RUSER}  
RUN adduser ${RUSER} sudo  
USER ${RUSER}  
WORKDIR /home/${RUSER}  
  
# Install g2o  
COPY external/g2o /home/${RUSER}/code/g2o  
RUN sudo chown -R ${RUSER}:${RUSER} /home/${RUSER}  
  
WORKDIR /home/${RUSER}/code/g2o  
RUN mkdir build  
WORKDIR /home/${RUSER}/code/g2o/build  
RUN cmake ..  
RUN make -j$(nproc --ignore=1 ) # building g2o might take awhile...  
RUN sudo make install  
  
RUN sudo install_clean \  
python-pip python-setuptools  
  
RUN sudo pip install --no-cache-dir --upgrade pip  
RUN sudo pip install --no-cache-dir platformio  
  
# vim: set syntax=dockerfile:  

