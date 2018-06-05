FROM ubuntu:16.04  
MAINTAINER Eduard Saller (www.saller.io)  
  
## Install zsh, vim, git, mosh, ack and build-essential  
RUN apt-get update && apt-get upgrade && \  
apt-get install -y vim zsh git ssh mosh ack-grep locales build-essential && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Switch to zsh ass default shell  
RUN chsh -s `which zsh`  
  
# move into setup script  
ENV TERM=xterm-256color  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
## Copy startup script  
COPY app /app  
# Make sure we can run it  
RUN chmod +x /app/vimwiki/run.sh  
  
# Required to not get a 'Missing privilege separation directory' error  
RUN mkdir /var/run/sshd  
  
# Set the data location inside the container (if you want to change this)  
ARG VIMWIKIDATA  
ENV VIMWIKIDATA ${VIMWIKIDATA:-/data/vimwiki}  
  
# Set container volumes  
VOLUME ["${VIMWIKIDATA}"]  
# Expose mosh ports  
EXPOSE 60000-61000  
# Expose container ssh  
EXPOSE 22  
# Add Tini  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--", "/app/vimwiki/run.sh"]  

