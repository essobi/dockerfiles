FROM ubuntu  
  
RUN apt-get update && apt-get install -y git python default-jre wget unzip
build-essential libz-dev ncbi-blast+  
RUN git clone https://github.com/mrmckain/fast-plast.git  
RUN cd /fast-plast && echo -e "n\nall" | perl INSTALL.pl  
VOLUME /data  
WORKDIR /data

