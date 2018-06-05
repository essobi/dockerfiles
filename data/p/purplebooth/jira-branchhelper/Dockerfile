FROM golang:1.9  
ENV VERSION_STRING=docker  
RUN mkdir -p /go/src/github.com/PurpleBooth/jira-branch-helper  
WORKDIR /go/src/github.com/PurpleBooth/jira-branch-helper  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN go get github.com/onsi/ginkgo/ginkgo  
RUN go get github.com/onsi/gomega  
COPY . .  
RUN dep ensure  
RUN (cd jira/branchhelper && go test)  
RUN go build -o binary \  
-ldflags "-linkmode external -extldflags -static -X main.AppVersion=$VERSION_STRING" \  
-a \  
cmd/jira-branch-helper/jira-branch-helper.go  
  
FROM scratch  
COPY \--from=0 /go/src/github.com/PurpleBooth/jira-branch-helper/binary /jira-
branch-helper  
ENTRYPOINT ["/jira-branch-helper"]  

