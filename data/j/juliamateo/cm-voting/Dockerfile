# Use the official go docker image built on debian.  
FROM golang  
  
#Install dnsutils  
RUN apt-get update && \  
apt-get install -q -y dnsmasq dnsutils  
  
# Install revel and the revel CLI.  
RUN go get github.com/revel/revel \  
github.com/revel/cmd/revel \  
gopkg.in/mgo.v2 \  
golang.org/x/crypto/bcrypt  
  
CMD ["revel", "run", "github.com/karesti/cm-voting", "prod", "9000"]  
  
# Open up the port where the app is running.  
EXPOSE 9000  
# Grab the source code and add it to the workspace.  
ADD . /go/src/github.com/karesti/cm-voting  
  
ADD ./app/db/agenda.json /go/app/db/agenda.json  

