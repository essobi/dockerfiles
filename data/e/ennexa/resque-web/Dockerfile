# Set the base image to Debian:wheezy  
FROM debian:jessie  
  
# Install wget, sox and flite  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y ruby ruby-dev zlib1g-dev build-essential && \  
gem install resque-web && \  
apt-get autoremove -y ruby-dev zlib1g-dev build-essential && \  
apt-get clean -y  
  
ENTRYPOINT ["resque-web", "-FL"]  
EXPOSE 5678  
  
CMD ["-h"]  
  
WORKDIR /data

