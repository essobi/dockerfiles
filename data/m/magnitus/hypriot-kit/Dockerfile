FROM python:2.7-slim-stretch  
  
ENV WORKSPACE /opt/app  
ENV HYPRIOT_ARTIFACTS_VOLUME hypriot-artifacts  
ENV HYPRIOT_ARTIFACTS_VOLUME_PATH $WORKSPACE/artifacts  
ENV VERBOSITY=quiet  
  
RUN apt-get update && apt-get install -y curl git && apt-get clean  
  
RUN curl
https://download.docker.com/linux/static/stable/x86_64/docker-17.12.1-ce.tgz >
/opt/docker.tgz && \  
cd /opt/ && tar -xf docker.tgz && mv docker/docker /usr/bin && chmod +x
/usr/bin/docker && rm -rf docker docker.tgz  
  
COPY scripts/*.py configs.json requirements.txt $WORKSPACE/  
  
WORKDIR $WORKSPACE  
  
RUN pip install -r requirements.txt  
  
CMD ["python", "-u", "build.py"]  

