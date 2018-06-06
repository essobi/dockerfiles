FROM ubuntu:16.04  
ENV PACKAGES python-dev git python-setuptools python-pip  
  
ENV BRANCH=develop  
ENV VERSION=6ba6a3ebde81fe8ed4d0c231ab42c613aa03334f  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ${PACKAGES}  
  
RUN git clone -b ${BRANCH} git://github.com/Sage-
Bionetworks/synapsePythonClient.git && \  
cd synapsePythonClient && \  
git checkout ${VERSION} && \  
python setup.py develop  
  
COPY challenge.py /challenge.py  
COPY challenge_config.py /challenge_config.py  
COPY lock.py /lock.py  
COPY messages.py /messages.py  
COPY runTool.sh /runTool.sh  
COPY runWriteUpCopyTool.py /runWriteUpCopyTool.py

