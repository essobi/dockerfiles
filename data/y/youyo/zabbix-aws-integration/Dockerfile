FROM golang:1 AS build-env  
LABEL maintainer "youyo <1003ni2@gmail.com>"  
  
ENV Owner youyo  
ENV Name zabbix-aws-integration  
ENV Repository github.com/${Owner}/${Name}  
ENV DIR /go/src/${Repository}  
  
WORKDIR ${DIR}  
  
ADD . ${DIR}  
RUN go get -u -v github.com/golang/dep/cmd/dep github.com/mitchellh/gox  
RUN dep ensure -v  
RUN Version=`git describe --tags --abbrev=0` \  
CommitHash=`git rev-parse --verify HEAD` \  
BuildTime=`date '+%Y/%m/%d %H:%M:%S %Z'` \  
GoVersion=`go version` \  
go build \  
-ldflags="\  
-X \"${Repository}/cmd/${Name}/cmd.Name=${Name}\" \  
-X \"${Repository}/cmd/${Name}/cmd.Version=${Version}\" \  
-X \"${Repository}/cmd/${Name}/cmd.CommitHash=${CommitHash}\" \  
-X \"${Repository}/cmd/${Name}/cmd.BuildTime=${BuildTime}\" \  
-X \"${Repository}/cmd/${Name}/cmd.GoVersion=${GoVersion}\"\  
" \  
-o ./pkg/${Name} \  
./cmd/${Name}/  
  
FROM zabbix/zabbix-agent:centos-trunk  
LABEL maintainer "youyo <1003ni2@gmail.com>"  
  
ENV Owner youyo  
ENV Name zabbix-aws-integration  
ENV Repository github.com/${Owner}/${Name}  
ENV DIR /go/src/${Repository}  
  
COPY \--from=build-env ${DIR}/pkg/${Name} /var/lib/zabbix/bin/${Name}  
ADD zabbix-aws-integration.conf /etc/zabbix/zabbix_agentd.d/  
EXPOSE 10050/TCP  
WORKDIR /var/lib/zabbix  
ENTRYPOINT ["docker-entrypoint.sh"]  

