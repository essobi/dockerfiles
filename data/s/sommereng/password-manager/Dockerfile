FROM golang  
  
# First layer to create the certificate:  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y openssl && \  
cd /home && \  
openssl genrsa -out server.key 4096 && \  
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 3650
-subj "/C=DE/ST=Denial/L=Springfield/O=Dis/CN=My own" && \  
apt-get autoremove -y openssl  
  
# Update the operating system and install base tools as second layer. Thus,
the first layer could stay longer without changes.  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
# Insert all files from the repo (but from the current directory, not from
Git):  
ADD . /go/src/github.com/SommerEngineering/PasswordManager/  
  
# Compile and Setup  
RUN \  
  
cd /go/src/github.com/SommerEngineering/PasswordManager && \  
  
# Add dependencies:  
go get github.com/twinj/uuid && \  
go get github.com/howeyc/gopass && \  
  
# Compile the code:  
go install && \  
  
# Copy the final binary and the runtime scripts to the home folder:  
cp /go/bin/PasswordManager /home && \  
cp /go/src/github.com/SommerEngineering/PasswordManager/run.sh /home/run.sh &&
\  
  
# Uninstall tools:  
apt-get autoremove -y zip openssl && \  
  
# Delete the entire Go workspace:  
rm -r -f /go && \  
  
# Make the scripts executable:  
chmod 0777 /home/run.sh && \  
chmod 0777 /home/PasswordManager && \  
mkdir /home/artifacts && \  
chmod 0777 /home/artifacts  
  
# Run anything below as nobody:  
USER nobody  
  
# Service provides HTTPS by port 60000:  
EXPOSE 60000  
  
# Configuration:  
ENV PASSWORD_MANAGER_MASTER_PASSWORD="MASTER PASSWORD"  
ENV PASSWORD_MANAGER_WEB_PASSWORD="PASSWORD"  
# Artifacts stored here:  
VOLUME /home/artifacts  
  
# Define the working directory:  
WORKDIR /home  
  
# The default command to run, if a container starts:  
CMD ["./run.sh"]

