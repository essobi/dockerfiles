FROM golang  
  
# Update the operating system and install base tools:  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y zip  
  
# Insert all files from the repo (but from the current directory, not from
Git):  
ADD . /go/src/github.com/SommerEngineering/WebProxy/  
  
# Compile and Setup  
RUN cd /go/src/github.com/SommerEngineering/WebProxy && \  
  
# Compile the code:  
go install && \  
  
# Copy the final binary and the runtime scripts to the home folder:  
cp /go/bin/WebProxy /home && \  
cp /go/src/github.com/SommerEngineering/WebProxy/run.sh /home/run.sh && \  
  
# Uninstall tools:  
apt-get autoremove -y zip && \  
  
# Delete the entire Go workspace:  
rm -r -f /go && \  
  
# Make the program and scripts executable:  
chmod 0777 /home/WebProxy && \  
chmod 0777 /home/run.sh  
  
# Run anything below as nobody:  
USER nobody  
  
# Service provides HTTP by port 50000:  
EXPOSE 50000  
  
ENV CONFIGURATION="myhost1=>http://www.another-domain.com
myhost2=>http://www.test.com"  
# Define the working directory:  
WORKDIR /home  
  
# The default command to run, if a container starts:  
CMD ["./run.sh"]

