FROM varikin/golang-glide-alpine AS build  
WORKDIR /go/src/github.com/k8guard/k8guard-report  
COPY ./ ./  
RUN apk -U add make  
RUN make deps build  
  
FROM alpine  
RUN apk -U add ca-certificates  
COPY \--from=build /go/src/github.com/k8guard/k8guard-report/k8guard-report /  
COPY \--from=build /go/src/github.com/k8guard/k8guard-report/templates
/templates  
EXPOSE 3001  
ENTRYPOINT ["/k8guard-report"]  

