FROM circleci/golang:1.9.0  
LABEL maintainer "Works Applications Co., Ltd."  
  
ENV PATH=/usr/lib/google-cloud-sdk/bin:/usr/lib/google-cloud-
sdk/platform/google_appengine:$PATH  
ENV GOPATH=/go  
  
RUN sudo apt-get update && \  
sudo apt-get install -y unzip && \  
sudo rm -rf /var/lib/apt/lists/*  
  
RUN curl -ssl https://sdk.cloud.google.com | sudo bash -s -- --disable-prompts
--install-dir=/usr/lib && \  
gcloud config set core/disable_usage_reporting true && \  
gcloud config set component_manager/disable_update_check true && \  
gcloud config set metrics/environment github_docker_image && \  
\  
sudo /usr/lib/google-cloud-sdk/bin/gcloud components install \  
app-engine-go \  
cloud-datastore-emulator && \  
\  
sudo chmod +x \  
/usr/lib/google-cloud-sdk/platform/google_appengine/goapp \  
/usr/lib/google-cloud-sdk/platform/google_appengine/godoc \  
/usr/lib/google-cloud-sdk/platform/google_appengine/gofmt \  
/usr/lib/google-cloud-sdk/platform/google_appengine/appcfg.py  
  
RUN go get -v github.com/axw/gocov/gocov && \  
go get -v github.com/mattn/goveralls && \  
go get -v github.com/golang/lint/golint && \  
go get -v golang.org/x/tools/cmd/goimports  
  
RUN curl https://glide.sh/get | sh  

