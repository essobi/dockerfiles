FROM alpine:3.7 as downloader  
RUN wget
http://download.adaptec.com/raid/storage_manager/arcconf_v2_05_22932.zip -O
/tmp/arcconf_v2_05_22932.zip && \  
unzip /tmp/arcconf_v2_05_22932.zip -d /tmp && \  
chmod +x /tmp/linux_x64/static_arcconf/cmdline/arcconf  
  
FROM golang:1.10-alpine as builder  
COPY gosrc /go/src/arccheck  
WORKDIR /go/src/arccheck  
RUN apk add --no-cache git gcc libc-dev && \  
go get && \  
GO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -tags netgo
-installsuffix netgo -ldflags '-w' -o arccheck .  
  
FROM alpine:3.7  
LABEL maintainer "benj.saiz@gmail.com"  
COPY \--from=downloader /tmp/linux_x64/static_arcconf/cmdline/arcconf
/usr/bin/arcconf  
COPY \--from=builder /go/src/arccheck/arccheck /usr/bin/arccheck  
RUN apk add --no-cache perl ca-certificates && \  
apk add --no-cache --virtual=build-dependencies perl-utils build-base && \  
cpan install -y File::Which && \  
apk del --purge build-dependencies  
RUN wget https://raw.githubusercontent.com/DisasteR/check_adaptec_raid/case-
fix/check_adaptec_raid -O /usr/bin/check_adaptec_raid && \  
chmod +x /usr/bin/check_adaptec_raid  

