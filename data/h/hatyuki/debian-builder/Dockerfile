# Pull base image  
FROM debian:latest  
  
# Install packages  
RUN apt-get update && apt-get install --yes --no-install-recommends \  
ca-certificates \  
debootstrap \  
git-core \  
xz-utils && \  
find /var/cache -type f -exec rm -f {} \; && \  
find /var/lib/apt -type f -exec rm -f {} \; && \  
find /var/log -type f | while read f; do :> $f; done;  
  
# Create working directory  
RUN mkdir -p /docker  
  
# Copy build script  
COPY files/build.sh /docker/build.sh  
  
# Define mountable directories  
VOLUME ["/docker/image"]  
  
# Define working directory  
WORKDIR /docker  
  
# Define default entrypoint  
ENTRYPOINT ["/bin/bash", "-eu", "./build.sh"]  
  
# Define default command  
CMD ["/bin/bash"]  

