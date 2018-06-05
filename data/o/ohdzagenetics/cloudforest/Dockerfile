# Header  
FROM ohdzagenetics/phyluce  
  
ENV PHYBASE_VERSION "1.5"  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
phyml \  
r-base-core \  
r-cran-ape && \  
pip3 install rpy2 dendropy mrjob  
  
# Install Phybase  
ADD
http://faculty.franklin.uga.edu/lliu/sites/faculty.franklin.uga.edu.lliu/files/phybase_$PHYBASE_VERSION.tar.gz
\  
phybase.tar.gz  
RUN R CMD INSTALL phybase.tar.gz  
  
# Install CloudForest  
ADD . /src/  
WORKDIR /src/  
RUN python setup.py build && python setup.py install  
  
# Add additional pieces of CloudForest to PATH  
RUN echo 'alias cloudforest_mpi.py="python
/src/cloudforest/cloudforest_mpi.py"' >> ~/.bashrc && \  
echo 'alias nexus2oneliner.py="python /src/cloudforest/nexus2oneliner.py"' >>
~/.bashrc && \  
echo 'alias phybase.py="python /src/cloudforest/phybase.py"' >> ~/.bashrc && \  
echo 'alias phylip2oneliner.py="python /src/cloudforest/phylip2oneliner.py"'
>> ~/.bashrc && \  
echo 'alias process.py="python /src/cloudforest/process.py"' >> ~/.bashrc  
  
# Add short BASH scripts to PATH for non-interactive use  
RUN echo '#!/bin/bash cloudforest_mpi.py' > /usr/bin/cloudforest_mpi.py && \  
chmod +x /usr/bin/cloudforest_mpi.py && \  
echo '#!/bin/bash nexus2oneliner.py' > /usr/bin/nexus2oneliner.py && \  
chmod +x /usr/bin/nexus2oneliner.py && \  
echo '#!/bin/bash phybase.py' > /usr/bin/phybase.py && \  
chmod +x /usr/bin/phybase.py && \  
echo '#!/bin/bash phylip2oneliner.py' > /usr/bin/phylip2oneliner.py && \  
chmod +x /usr/bin/phylip2oneliner.py && \  
echo '#!/bin/bash process.py' > /usr/bin/process.py && \  
chmod +x /usr/bin/process.py  

