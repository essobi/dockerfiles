FROM debian:sid  
RUN apt-get update && apt-get -y upgrade && apt-get -y install git build-
essential qemu qemu-kvm  
RUN git clone https://github.com/intel/lkp-tests.git  
RUN cd /lkp-tests && make install  
RUN yes | lkp install  

