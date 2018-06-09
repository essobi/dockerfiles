FROM alpine:3.7  
RUN apk --no-cache add nginx curl jq bash coreutils && \  
mkdir -p /run/nginx /www  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /app  
ADD *.sh repos.txt ./  
RUN ./check_github_releases.sh  
  
ADD cronjob.sh /etc/periodic/hourly/run_bash_script  
#ADD cronjob.sh /etc/periodic/15min/run_bash_script  
EXPOSE 80  
ENTRYPOINT ["./entrypoint.sh"]  
  

