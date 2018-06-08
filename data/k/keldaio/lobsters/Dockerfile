# This container is based on the Ruby image, which means that it  
# automatically inherits the Ruby installation defined in that image.  
FROM ruby:2.3.1  
# Install NodeJS and cmake, which are required by lobste.rs.  
RUN apt-get update && apt-get install nodejs cmake -y  
  
# Download and build the lobste.rs code.  
RUN git clone git://github.com/jcs/lobsters.git  
WORKDIR lobsters  
RUN bundle  
  
# Add a file to the container that contains startup code for lobste.rs. This  
# command assumes that start-lobsters.sh is in the same directory as this  
# Dockerfile  
COPY start-lobsters.sh /lobsters/  
  
# When the container starts, it should run the lobste.rs server using the  
# start-lobsters.sh bash file that we copied above. This is a common  
# "gotcha" to people new to containers: unlike VMs, each container is based  
# on a process (in this case, rails, which is started at the end of  
# start-lobsters.sh) and will be shutdown when that process stops.  
ENTRYPOINT ["/bin/sh", "/lobsters/start-lobsters.sh"]  

