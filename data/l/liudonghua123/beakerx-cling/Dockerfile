FROM beakerx/beakerx  
  
MAINTAINER liudonghua123 <liudonghua123@gmail.com>  
  
USER root  
  
# install gcc7  
RUN add-apt-repository -y ppa:jonathonf/gcc-7.2  
RUN apt-get update -y  
RUN apt-get install -y gcc-7  
# create gcc alias to gcc-7  
RUN cd /usr/bin && ln -s gcc-7 gcc  
  
#RUN source activate beakerx && conda install xeus-cling notebook -c
QuantStack -c conda-forge -y  
RUN ["/bin/bash", "-c", "source activate beakerx && conda info --envs && conda
install xeus-cling notebook -c QuantStack -c conda-forge -y"]  
  
# revert to the default beakerx user  
USER beakerx  

