FROM xarthisius/girder:latest  
MAINTAINER Kacper Kowalik <xarthisius.kk@gmail.com>  
  
# RUN git clone https://github.com/data-exp-lab/girder_ythub
/girder/plugins/ythub -b dev  
COPY ./plugin.yml /girder/plugins/ythub/plugin.yml  
COPY ./requirements.txt /girder/plugins/ythub/requirements.txt  
COPY ./server /girder/plugins/ythub  
COPY ./web_client /girder/plugins/ythub  
  
WORKDIR /girder  
  
RUN girder-install plugin plugins/ythub  
RUN girder-install web --plugins=ythub  
  
COPY ./girder.ythub.cfg /girder/girder/conf/girder.local.cfg  

