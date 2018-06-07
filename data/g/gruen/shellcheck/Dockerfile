#  
# Run shellcheck inside a docker container  
# docker run -i --rm \  
# -v "$(pwd)":/workdir \  
# --name [name] \  
# gruen\shellcheck file_to_check [options]  
#  
FROM debian:jessie  
LABEL maintainer "Darren Green <darren@gruen.site>"  
RUN apt-get update \  
&& apt-get install -y shellcheck \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/workdir"]  
WORKDIR /workdir  
  
ENTRYPOINT ["shellcheck"]  

