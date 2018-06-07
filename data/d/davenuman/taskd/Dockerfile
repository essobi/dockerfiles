FROM debian:stable-slim  
  
RUN apt-get update && apt-get install -y apt-utils git gcc g++ gnutls-bin
cmake libgnutls28-dev uuid-dev  
  
# Clone taskd git repo  
RUN git clone https://git.tasktools.org/TM/taskd.git taskd-build  
WORKDIR /taskd-build  
  
# compile taskd  
RUN cmake -DCMAKE_BUILD_TYPE=release .  
RUN make  
  
# Run tests  
#WORKDIR /taskd-build/test  
#RUN make && ./run_all  
# Install taskd  
WORKDIR /taskd-build  
RUN make install  
  
# Clean up build tools  
RUN apt-get remove -y apt-utils git gcc g++ libgnutls28-dev uuid-dev cmake &&
\  
apt-get autoclean -y && apt-get autoremove -y  
  
# Create user and verify that taskd is installed  
ENV TASKDDATA /data/taskd  
VOLUME /data  
RUN useradd -d $TASKDDATA taskd  
RUN taskd --version  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 53589  

