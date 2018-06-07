FROM ubuntu:xenial  
  
# Install some build dependencies  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
wget \  
default-jre \  
apt-transport-https  
  
# Install handbrake  
RUN add-apt-repository ppa:stebbins/handbrake-releases \  
&& apt-get update \  
&& apt-get install -y handbrake-cli  
  
# Install mkvtoolnix  
RUN wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | apt-
key add - \  
&& echo "deb https://mkvtoolnix.download/ubuntu/ xenial main" >
/etc/apt/sources.list.d/bunkus.org.list \  
&& apt-get update \  
&& apt-get install -y mkvtoolnix  
  
# Make some internal directories  
RUN mkdir -p /opt/transcode/scripts && mkdir -p /opt/transcode/working  
  
# Copy scripts into place  
WORKDIR /opt/transcode/scripts  
COPY BDSup2Sub.jar transcode-movie.sh transcode-tvseries.sh entrypoint.sh ./  
  
# Set up volume for input files and volume for output files of each kind  
VOLUME /input  
VOLUME /movies  
VOLUME /tv  
  
ENTRYPOINT ["/opt/transcode/scripts/entrypoint.sh"]  

