FROM ubuntu:14.04  
MAINTAINER Matthew McKeen <matthew@mmckeen.net>  
  
RUN apt-get update && apt-get upgrade -y  
# Install dependencies  
RUN apt-get install -y git wget  
  
# Clone source, checkout latest release and build  
# On a single line so resultant image is as small as possible  
RUN git clone https://github.com/facebook/osquery.git && cd osquery && git
checkout $(git describe --tags `git rev-list \--tags \--max-count=1`) &&
./tools/provision.sh && make && make package && dpkg -i
./build/linux/osquery-$(git describe --tags `git rev-list \--tags \--max-
count=1`).deb && cd .. && rm -rf osquery  
  
# When container starts, start osqueryi  
CMD /usr/bin/osqueryi  

