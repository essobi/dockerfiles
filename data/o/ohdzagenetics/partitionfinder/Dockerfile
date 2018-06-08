# Header  
FROM ubuntu:latest  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
phyml \  
python \  
python-pip \  
python-pytest \  
raxml  
  
RUN pip install numpy \  
pandas \  
tables \  
pyparsing \  
scipy \  
sklearn  
  
# Mount code  
COPY . /src  
  
WORKDIR /src  
  
# "Install" by setting up aliases  
RUN echo 'alias PartitionFinder="python /src/PartitionFinder.py"' >> ~/.bashrc
&& \  
echo 'alias PartitionFinderMorphology="python
/src/PartitionFinderMorphology.py"' >> ~/.bashrc && \  
echo 'alias PartitionFinderProtein="python /src/PartitionFinderProtein.py"' >>
~/.bashrc  
  
# Add short BASH scripts to PATH for non-interactive use  
RUN echo '#!/bin/bash PartitionFinder' > /usr/bin/PartitionFinder && \  
chmod +x /usr/bin/PartitionFinder && \  
echo '#!/bin/bash PartitionFinderMorphology' >
/usr/bin/PartitionFinderMorphology && \  
chmod +x /usr/bin/PartitionFinderMorphology && \  
echo '#!/bin/bash PartitionFinderProtein' > /usr/bin/PartitionFinderProtein &&
\  
chmod +x /usr/bin/PartitionFinderProtein  
  
# Run tests  
#RUN make test  

