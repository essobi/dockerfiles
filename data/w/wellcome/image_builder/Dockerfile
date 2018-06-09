FROM wellcome/build_tooling  
  
LABEL maintainer "Alex Chan <a.chan@wellcome.ac.uk>"  
LABEL description "A Docker image for building Docker images for the Wellcome
Digital Platform"  
  
RUN pip3 install docopt boto3  
  
COPY . /builds  
  
VOLUME /repo  
WORKDIR /repo  
  
ENTRYPOINT ["python3", "/builds/build_docker_image.py"]  

