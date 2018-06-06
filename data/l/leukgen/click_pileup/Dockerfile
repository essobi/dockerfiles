FROM leukgen/docker-vafcorrect:v0.1.1  
# set mantainers  
LABEL maintainers="github.com/jsmedmar, github.com/juanesarango"  
  
# install repo  
COPY . /code  
RUN pip3 install /code && rm -rf /code  
  
# create a /ifs volume for MSK users  
VOLUME /ifs  
VOLUME /data  
  
# see: https://github.com/BD2KGenomics/cgl-docker-lib  
WORKDIR /data  
  
# set entrypoint  
ENTRYPOINT [ "click_pileup" ]  

