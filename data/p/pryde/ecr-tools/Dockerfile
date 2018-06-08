# Build image  
FROM golang:1.10.2-alpine AS build-env  
ARG NAME=ecr-tools  
ARG DESCRIPTION="ECR Docker Token"  
ARG URL="https://pryde.app"  
ARG ORG=lyon-pryde  
ARG GO_SRC=/go/src/github.com/lyon/ecr-tools  
  
WORKDIR ${GO_SRC}  
RUN apk add ca-certificates git --update --no-cache  
RUN go get -u github.com/golang/dep/cmd/dep  
  
COPY Gopkg.toml .  
COPY Gopkg.lock .  
RUN dep ensure -vendor-only  
ADD . .  
  
WORKDIR ${GO_SRC}/cmd/ecr-tools  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/ecr-
tools -i .  
RUN ls /go/bin  
# # Test image  
# FROM golang:1.10.2-alpine AS test-env  
# WORKDIR /app  
# COPY --from=build-env /etc/ssl /etc/ssl  
# COPY --from=build-env ${GO_SRC}/bin/${NAME} /app/  
# RUN ls  
# Runtime image  
# FROM scratch  
FROM alpine  
# Metadata params  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_URL  
ARG VCS_REF  
ARG NAME=ecr-tools  
ARG ORG=lyon-pryde  
ARG VENDOR  
  
# Metadata  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name=lyon-pryde \  
org.label-schema.description=${DESCRIPTION} \  
org.label-schema.url=${URL}\  
org.label-schema.vcs-url=https://github.com/lyon-pryde/$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vendor=$VENDOR \  
org.label-schema.version=$VERSION \  
org.label-schema.docker.schema-version="1.0" \  
org.label-schema.docker.cmd="docker run -d lyon-pryde/ecr-tools"  
WORKDIR /app  
COPY \--from=build-env /etc/ssl /etc/ssl  
COPY \--from=build-env /go/bin/ecr-tools /app/ecr-tools  
ENTRYPOINT ["/app/ecr-tools"]

