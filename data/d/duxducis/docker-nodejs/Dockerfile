FROM debian:jessie  
  
RUN apt-get update  
  
RUN apt-get install -y curl  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
git-core \  
build-essential \  
ruby \  
nodejs \  
libkrb5-dev  
  
RUN gem install tiller  
  
# Set the entry point  
ENTRYPOINT ["/init"]  
  
EXPOSE 5000  
# Install services  
COPY services /etc/services.d  
  
# Install init.sh as init script  
COPY init.sh /etc/cont-init.d/  
  
# Copy tiller configuration  
COPY data /etc/tiller  
  
# Link to ssh key location  
RUN mkdir /root/.ssh && chmod 700 /root/.ssh && ln -s /deployment.key
/root/.ssh/id_rsa  
  
#RUN touch /etc/services.d/app/down  
# Download and extract s6 init  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.10.0.3/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  

