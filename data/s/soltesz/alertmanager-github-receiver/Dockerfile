FROM golang:1.8  
RUN go get -v github.com/stephen-soltesz/alertmanager-github-
receiver/cmd/github_receiver  
# COPY . /go/src  
# RUN go get -d -v cmd/github_receiver  
# RUN go install -v  
ENTRYPOINT ["/go/bin/github_receiver"]  

