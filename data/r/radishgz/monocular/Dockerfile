FROM quay.io/deis/go-dev:v0.22.0  
MAINTAINER Miguel Martinez <miguel@bitnami.com>  
  
RUN curl https://glide.sh/get | sh  
  
COPY rootfs/ /  
  
WORKDIR /go/src/github.com/helm/monocular/src/api  
  
ENV HOST=0.0.0.0  
ENV PORT=8080  
RUN cd / && git clone http://github.com/helm/monocular/  
#RUN cd / && git clone https://gitlab.com/gitlab-org/gitlab-ci-multi-
runner.git  
RUN mkdir -p /go/src/github.com/helm/monocular/src/api/vendor  
RUN cp -R /monocular/src/api /go/src/github.com/helm/monocular/src/  
#RUN cp -R /gitlab-ci-multi-runner/vendor/k8s.io
/go/src/github.com/helm/monocular/src/api/vendor/k8s.io  
WORKDIR /go/src/github.com/helm/monocular/src/api  
  
ENV HOST=0.0.0.0  
ENV PORT=8080  
#RUN go get github.com/helm/monocular/src/api  
#RUN curl -sL
https://github.com/kardianos/govendor/releases/download/v1.0.8/govendor_linux_amd64
-o /usr/bin/govendor  
#RUN chmod +x /usr/bin/govendor  
#RUN govendor init  
#RUN govendor fetch -v +all  
RUN cd /go/src/github.com/helm/monocular/src/api && glide install  
#RUN cd /go/src/github.com/helm/monocular/src/api && go build .  
ENTRYPOINT ["/app-entrypoint.sh"]  
  
CMD ["go", "run", "main.go"]  

