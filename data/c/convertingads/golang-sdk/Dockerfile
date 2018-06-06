FROM golang:1-stretch  
RUN apt-get update && \  
apt-get -y install python wget unzip git && \  
go get -u github.com/golang/dep/cmd/dep && \  
go get github.com/pilu/fresh && \  
go get github.com/go-swagger/go-swagger/cmd/swagger && \  
go get github.com/derekparker/delve/cmd/dlv && \  
cd / && \  
wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip &&
\  
unzip google-cloud-sdk.zip && \  
rm google-cloud-sdk.zip && \  
google-cloud-sdk/install.sh \--usage-reporting=true --path-update=true --bash-
completion=true --rc-path=/.bashrc --additional-components app kubectl alpha
beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-engine-go
bigtable docker-credential-gcr && \  
google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true && \  
apt-get -y clean  
  

