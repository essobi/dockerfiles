FROM alpine:3.5  
MAINTAINER pasi@pashi.net  
  
RUN apk add --update python3 py3-pillow  
RUN pip3 install acdcli  
RUN mkdir -p /root/.cache/acd_cli /app ; ln -s /oauth_data
/root/.cache/acd_cli/oauth_data  
VOLUME ["/app"]  
WORKDIR /app  
ENTRYPOINT ["/bin/sh"]  

