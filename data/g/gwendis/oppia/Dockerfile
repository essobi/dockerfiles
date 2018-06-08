FROM ubuntu  
  
RUN mkdir /root/opensource  
WORKDIR /root/opensource  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
icedtea-8-plugin \  
openjdk-8-jre \  
python \  
python-pip \  
sudo \  
unzip  
RUN pip install gitpython  
  
RUN git clone https://github.com/oppia/oppia.git  
  
WORKDIR /root/opensource/oppia  
RUN git checkout develop  
  
RUN bash scripts/install_prerequisites.sh  
RUN bash scripts/setup.sh  
RUN TOOLS_DIR="/root/opensource/oppia_tools" bash scripts/setup_gae.sh  
RUN bash scripts/install_third_party.sh  
RUN rm -rf /root/opensource/node_modules/through2  
RUN sed -i "75i storage_path: '/tmp/appengine.oppiaserver.root'," gulpfile.js  
  
CMD ["bash", "scripts/start.sh", "--save_datastore"]  
  
EXPOSE 8000 8181

