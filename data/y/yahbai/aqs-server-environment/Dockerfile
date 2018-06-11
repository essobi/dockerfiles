####################################################################################################  
#  
# This dockerfile is built off the official mongodb (v3.6.1) dockerfile for
debian, as of jan 2018.  
# (see https://hub.docker.com/_/mongo/)  
#  
# it uses debian v8 (jessie) because that's the most recent debian that mongo
supports (doh!).  
# can't get it to run on latest debian because no one can right now (ssl lib
incompatability)  
#  
# jessie is also the version that node latest is built off.  
#  
# it currently uses java v7, because that's the most recent that had a
dockerfile for jessie  
#  
# it then kludges in the dockerfile commands for openjdk and node, and then
finally does any setup  
# that AQS itself wants (e.g. install dcmtk).  
#  
# docker files and versions used (name, version, docker hub tag, link to
github docker build)  
#  
# openjdk 7u141 7, 7-jdk https://github.com/openjdk/7-jdk  
# node 9 9, latest https://github.com/nodejs/docker-node  
#  
# finally it installs anything needed/wanted for AQS.  
# right now that includes git and dcmtk  
#  
####################################################################################################  
  
  
FROM debian:latest  
  
RUN apt-get update  
  
RUN mkdir /tmp/retrieved_files  
  
RUN apt-get install -y \  
bzip2 \  
unzip \  
gpg \  
xz-utils \  
git \  
ftp-ssl \  
dcmtk \  
build-essential \  
curl \  
xz-utils \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
openjdk-8-jdk \  
&& rm -rf /var/lib/apt/lists/*  
  
  
####################################################################################################  
#  
# finished from openjdk dockerfile, now do node  
#  
####################################################################################################  
  
RUN apt-get update  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh  
RUN bash nodesource_setup.sh  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
RUN rm nodesource_setup.sh  
  
  
####################################################################################################  
#  
# finished from node dockerfile, now do ImageJ  
#  
####################################################################################################  
  
RUN curl http://wsr.imagej.net/distros/cross-platform/ij152.zip --output
ij152.zip  
RUN unzip ij152.zip -d /usr/local  
RUN rm ij152.zip  
  
####################################################################################################  
#  
# load anything else needed  
#  
####################################################################################################  
  
RUN npm i -g forever  
  
CMD ["bash"]  

