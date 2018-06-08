FROM alpine:latest  
LABEL maintainer="Syed Hassaan Ahmed"  
  
RUN apk add --update alpine-sdk openssl-dev curl && \  
rm -rf /var/cache/apk/* && \  
apk add --no-cache git && \  
git clone https://github.com/giltene/wrk2.git && \  
cd wrk2 && make && mv wrk /bin/  
  
ENV SCRIPT_URL ""  
ENV TARGET_URL ""  
ENV WRK_OPTIONS ""  
ENV WRK_HEADER "User-Agent: wrk"  
CMD ["sh", "-c", "if [ \"$SCRIPT_URL\" != \"\" ]; then curl -sS ${SCRIPT_URL}
> /tmp/script.lua; else echo \"\" > /tmp/script.lua; fi && wrk -s
/tmp/script.lua ${WRK_OPTIONS} -H \"${WRK_HEADER}\" ${TARGET_URL}"]

