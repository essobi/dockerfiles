FROM ubuntu:16.04  
MAINTAINER Sumner Evans  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Update the system  
RUN apt-get update && apt-get install -y python3 python3-pip ruby ruby-compass  
  
# Create a Bottle user.  
RUN groupadd web  
RUN useradd -d /home/wirelessdebug -m wirelessdebug  
  
# Add the source files to the user.  
WORKDIR /home/wirelessdebug  
ADD . .  
  
# Change into the server directory  
WORKDIR /home/wirelessdebug/server  
RUN cp -n sample-config.yaml config.yaml  
  
# Install the necessary packages.  
RUN gem install compass font-awesome-sass bootstrap-sass  
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt  
  
# Compile the CSS.  
RUN compass compile  
  
# Expose port 80 and run the application.  
EXPOSE 80  
ENTRYPOINT ["/home/wirelessdebug/server/widb_server.py"]  

