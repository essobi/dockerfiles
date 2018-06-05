# A Docker container for running phyluce  
FROM biopython/biopython  
  
RUN apt-get update && apt-get install -y \  
openjdk-8-jdk \  
openjdk-8-jre  
  
# Add source code  
ADD . /src/  
WORKDIR /src/  
  
RUN python setup.py install  

