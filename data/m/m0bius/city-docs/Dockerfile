# See => tianon/latex:latest on Dockerhub  
FROM tianon/latex  
# define enviroment variables  
ENV TERM xterm  
ENV DATA_PATH /tmp/cds  
# add project files to the image  
ADD . $DATA_PATH  
RUN chmod +x $DATA_PATH/Makefile  
# install make utility  
RUN apt-get update && apt-get install -y \  
make  
# move to the working directory  
WORKDIR $DATA_PATH  
# compile .tex files  
RUN make clean report.pdf  

