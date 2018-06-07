# use base image  
FROM leukgen/docker-strelka:v0.2.1  
# Define directories  
ENV OUTPUT_DIR /data  
ENV WORK_DIR /code  
ENV OPT_DIR /opt  
  
# Mount the output volume as persistant  
VOLUME ${OUTPUT_DIR}  
  
# set locale  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV CC /usr/bin/gcc-4.9  
ENV CXX /usr/bin/g++-4.9  
# install toil_strelka  
COPY . ${WORK_DIR}  
WORKDIR ${WORK_DIR}  
RUN pip install -r requirements.txt  
  
# set entrypoint  
ENTRYPOINT ["toil_strelka"]  

