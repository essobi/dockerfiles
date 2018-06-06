FROM golang:1.8-alpine  
RUN apk add --no-cache curl nodejs bash python wget unzip git  
RUN npm install gulp-cli -g  
RUN curl https://glide.sh/get | sh  
#RUN go get github.com/tools/godep  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app
kubectl alpha beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-
engine-go bigtable docker-credential-gcr  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  

