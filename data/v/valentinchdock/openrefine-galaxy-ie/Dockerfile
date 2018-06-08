FROM ubuntu:latest  
  
MAINTAINER Valentin Chambon "valentin.chambon@mnhn.fr"  
# These environment variables are passed from Galaxy to the container  
# and help you enable connectivity to Galaxy from within the container.  
# This means your user can import/export data from/to Galaxy.  
USER root  
ENV DEBIAN_FRONTEND=noninteractive \  
API_KEY=none \  
DEBUG=false \  
PROXY_PREFIX=none \  
GALAXY_URL=none \  
GALAXY_WEB_PORT=10000 \  
HISTORY_ID=none \  
REMOTE_HOST=none  
  
RUN apt-get update  
  
RUN apt-get install --no-install-recommends -y \  
wget procps nginx python python-pip net-tools nginx  
RUN apt-get install -y openjdk-8-jdk  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH="/usr/lib/jvm/java-8-openjdk-amd64/bin:${PATH}"  
RUN apt-get install -y python-pip  
RUN pip install --upgrade pip  
RUN pip install -U setuptools  
RUN pip install bioblend galaxy-ie-helpers  
  
#Vim to modify ass porky  
RUN apt-get install -y vim  
  
#Get urllib  
RUN wget -O - --no-check-certificate
https://github.com/ValentinChCloud/urllib2_file/archive/master.tar.gz | tar
-xz  
RUN mv urllib2_file-master urllib2_file; cd ./urllib2_file ; python setup.py
test  
RUN cd ./urllib2_file ; python setup.py build ; python setup.py install ;  
  
# Download and "mount" OpenRefine  
RUN wget -O - --no-check-certificate
https://github.com/ValentinChCloud/OpenRefine/archive/master.tar.gz |tar -xz  
RUN mv OpenRefine-master OpenRefine  
RUN apt-get install unzip  
  
RUN apt-get install -y curl  
  
# make some changes to Openrefine to export data to galaxy history  
ADD ./ExportRowsCommand.java
OpenRefine/main/src/com/google/refine/commands/project/ExportRowsCommand.java  
ADD ./exporters.js
OpenRefine/main/webapp/modules/core/scripts/project/exporters.js  
ADD ./langs/translation-default.json
OpenRefine/main/webapp/modules/core/langs/translation-default.json  
ADD ./langs/translation-fr.json
OpenRefine/main/webapp/modules/core/langs/translation-fr.json  
ADD ./langs/translation-fr.json
OpenRefine/main/webapp/modules/core/langs/translation-en.json  
  
RUN /OpenRefine/refine build  
  
#Get python api openrefine  
RUN wget -O - --no-check-certificate
https://github.com/ValentinChCloud/refine-python/archive/master.tar.gz | tar
-xz  
RUN mv refine-python-master refine-python  
  
#Import data  
ADD ./get_notebook.py /get_notebook.py  
  
# Our very important scripts. Make sure you've run `chmod +x startup.sh  
# monitor_traffic.sh` outside of the container!  
ADD ./startup.sh /startup.sh  
ADD ./monitor_traffic.sh /monitor_traffic.sh  
# Create and export project  
ADD ./openrefine_create_project_API.py /refine-
python/openrefine_create_project_API.py  
ADD ./openrefine_export_project.py /refine-python/openrefine_export_project.py  
  
# /import will be the universal mount-point for Jupyter  
# The Galaxy instance can copy in data that needs to be present to the  
# container  
RUN mkdir /import  
  
# Nginx configuration  
COPY ./proxy.conf /proxy.conf  
  
VOLUME ["/import"]  
WORKDIR /import/  
  
# EXTREMELY IMPORTANT! You must expose a SINGLE port on your container.  
EXPOSE 80  
CMD /startup.sh  

