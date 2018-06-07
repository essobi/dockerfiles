FROM zburgermeiszter/usermode:alpine-3.4  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
USER root  
  
RUN apk update && \  
apk add curl jq && \  
curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip >
ngrok.zip && \  
unzip ngrok.zip -d /usr/bin && \  
rm ngrok.zip  
  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
  
RUN chown user:user /usr/bin/ngrok && \  
chown user:user /usr/bin/entrypoint.sh && \  
chmod +x /usr/bin/entrypoint.sh  
  
USER user  
RUN mkdir -p /home/user/.ngrok2  
RUN echo "web_addr: 0.0.0.0:4040" > /home/user/.ngrok2/ngrok.yml  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

