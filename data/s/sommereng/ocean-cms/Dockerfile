FROM golang  
  
# Add Go's dep:  
RUN go get -u github.com/golang/dep/cmd/dep  
  
# Update the operating system:  
RUN \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y unzip nano libcap2-bin  
  
# Insert all files from the repo:  
ADD . /go/src/github.com/SommerEngineering/OceanCMS/  
  
# Compile and Setup:  
RUN \  
cd /go/src/github.com/SommerEngineering/OceanCMS && \  
#  
# Ensure all dependencies:  
dep ensure && \  
dep ensure -update && \  
#  
# Compile the code:  
go install && \  
#  
# Copy the final binary and the runtime scripts to the home folder:  
cp /go/bin/OceanCMS /home && \  
cp /go/src/github.com/SommerEngineering/OceanCMS/run.sh /home/run.sh && \  
cd ~ && \  
#  
# Delete the entire Go workspace:  
rm -r -f /go && \  
#  
# Make the scripts executable:  
chmod 0777 /home/run.sh && \  
chmod 0777 /home/OceanCMS &&\  
#  
# Allow binding on low ports:  
/sbin/setcap 'cap_net_bind_service=+ep' /home/OceanCMS  
  
# Run anything below as nobody:  
USER nobody  
  
# Service provides HTTPS by port 443:  
EXPOSE 443  
# Service provides HTTP by port 80:  
EXPOSE 80  
# Configuration:  
ENV OceanCMS_UseEnvironment="true"  
ENV OceanCMS_CertificateCAEMail=""  
ENV OceanCMS_SystemPassword=""  
ENV OceanCMS_ServerInterfacesPortHTTPS=":443"  
ENV OceanCMS_ServerInterfacesPortHTTP=":80"  
# Data stored here:  
VOLUME /home/data  
  
# Define the working directory:  
WORKDIR /home  
  
# The default command to run, if a container starts:  
CMD ["./run.sh"]

