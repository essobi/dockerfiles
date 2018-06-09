FROM nodesource/trusty:iojs-1.6.2  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y git software-properties-common  
RUN add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && apt-get install -y ffmpeg  
  
# Ensure git is installed (used by strong-pm)  
# Create "strong-pm" user  
RUN npm install \--unsafe-perm --global strongloop/strong-pm#production \  
&& npm cache clean \  
&& useradd -ms /bin/bash strong-pm  
  
# Set up some semblance of an environment  
WORKDIR /home/strong-pm  
ENV HOME /home/strong-pm  
  
# Run as non-privileged user inside container  
USER strong-pm  
  
# pre-load node-gyp to speed up build time of apps pushed to strong-pm  
# and remove need to download node source in production  
RUN node-gyp install 2> /dev/null && npm cache clear  
  
# Expose strong-pm port  
EXPOSE 8701  
  
ENTRYPOINT ["/usr/bin/sl-pm", "--base", ".", "--listen", "8701"]  

