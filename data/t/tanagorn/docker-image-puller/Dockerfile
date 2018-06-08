FROM python:2.7.13-slim  
  
ENV HOME=/usr/src/docker-image-updater/ \  
TEMP_APP=/tmp/app  
  
WORKDIR $HOME  
  
EXPOSE 9999  
# Install app dependencies  
COPY . $TEMP_APP  
  
# Build Application  
# Optimize images  
RUN mkdir -p ${HOME} \  
&& mkdir -p ${TEMP_APP} \  
&& cd ${TEMP_APP} \  
  
&& cp -a docker ${HOME} \  
&& cp app-swarm.py requirements.txt ${HOME} \  
&& pip install --no-cache-dir -r requirements.txt \  
&& apt-get clean  
  
ENTRYPOINT ["python", "-u", "app-swarm.py"]  

