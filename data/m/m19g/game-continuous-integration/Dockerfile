# If we need to build working image fast we can use trzeci/emscripten:latest
and  
# skip installing Emscripten, which takes a lot of time.  
FROM ubuntu:latest  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Copy our project from outside to inside Docker.  
WORKDIR ${HOME}/tmp  
COPY ./ ./  
# TODO: Is this necessary?  
# RUN chmod +x ./*.bash  
# Install dev dependencies  
RUN apt-get update && apt-get install sudo curl -y  
RUN ./install_or_update_dev_dependencies.bash  
  
# Build our project to populate Emscripten common library build cache  
RUN . /etc/profile && make build-dev -j$(nproc)  
RUN . /etc/profile && make build-prod -j$(nproc)  
  
WORKDIR ${HOME}/  
RUN rm -rf tmp  
  
# Docker can't use ulimit inside by default, and `service cassandra start`  
# attempts to use ulimit inside the following script so disable it.  
RUN sed -i 's/\\(^\s*ulimit\\)/#\1/' /etc/init.d/cassandra  
  
RUN mkdir /tmp  
RUN chmod 1777 /tmp  
ENV TMPDIR /tmp  

