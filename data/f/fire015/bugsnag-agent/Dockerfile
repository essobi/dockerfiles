FROM alpine:latest  
  
RUN apk add --update git curl python && rm -rf /var/cache/apk/*  
RUN curl -L http://git.io/q2AUSA | tee /usr/bin/bugsnag-agent && chmod +x
/usr/bin/bugsnag-agent  
  
EXPOSE 3829  
CMD /usr/bin/bugsnag-agent -p 3829 -l 0.0.0.0

