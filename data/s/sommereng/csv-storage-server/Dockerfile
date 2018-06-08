FROM golang  
  
# Update the operating system.  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
# Insert all files from the repo:  
ADD . /go/src/github.com/SommerEngineering/CSVStorageServer/  
  
# Compile and Setup  
RUN \  
  
cd /go/src/github.com/SommerEngineering/CSVStorageServer && \  
  
# Compile the code:  
go install && \  
  
# Copy the final binary and the runtime scripts to the home folder:  
cp /go/bin/CSVStorageServer /home && \  
cp /go/src/github.com/SommerEngineering/CSVStorageServer/run.sh /home/run.sh
&& \  
  
# Delete the entire Go workspace:  
rm -r -f /go && \  
  
# Make the scripts executable:  
chmod 0777 /home/run.sh && \  
chmod 0777 /home/CSVStorageServer && \  
mkdir /home/data && \  
chmod 0777 /home/data  
  
# Run anything below as nobody:  
USER nobody  
  
# Service provides HTTPS by port 50000:  
EXPOSE 50000  
# Configuration:  
ENV STORAGE_SERVER_DATA_DIRECTORY="data"  
ENV STORAGE_SERVER_WEB_BINDING=":50000"  
# Data stored here:  
VOLUME /home/data  
  
# Define the working directory:  
WORKDIR /home  
  
# The default command to run, if a container starts:  
CMD ["./run.sh"]

