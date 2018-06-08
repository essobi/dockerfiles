FROM dlanguage/dmd  
  
# Install operating system packages:  
RUN apt update && \  
  
#  
# Required for downloading Git LFS files:  
#  
apt install -y curl ca-certificates  
  
# Copy random data. As long as issue #500 (https://github.com/docker/hub-
feedback/issues/500) is unsolved,  
# it is necessary to use Git LFS manually to get the desired files.  
RUN \  
  
# Download the quantum numbers to the final destination:  
mkdir /quantum-numbers && \  
cd /quantum-numbers && \  
curl -O https://media.githubusercontent.com/media/SommerEngineering/quantum-
numbers/master/quantum-numbers01.random && \  
curl -O https://media.githubusercontent.com/media/SommerEngineering/quantum-
numbers/master/quantum-numbers02.random && \  
curl -O https://media.githubusercontent.com/media/SommerEngineering/quantum-
numbers/master/quantum-numbers03.random && \  
curl -O https://media.githubusercontent.com/media/SommerEngineering/quantum-
numbers/master/quantum-numbers04.random && \  
curl -O https://media.githubusercontent.com/media/SommerEngineering/quantum-
numbers/master/quantum-numbers05.random && \  
ls -lh  

