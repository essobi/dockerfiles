FROM debian AS DownloadContainer  
ADD https://bin.equinox.io/c/2ovkwS9YHaP/edgetunnels-stable-linux-amd64.tgz .  
RUN tar xzf *.tgz  
  
FROM debian  
  
LABEL maintainer="git@ashleypoole.co.uk"  
LABEL description="This is a Debian based Linux image containing Cloudflare
Warp"  
  
RUN mkdir /cloudflare-warp  
RUN mkdir /cloudflare-warp/tunnels  
  
WORKDIR /cloudflare-warp  
  
COPY \--from=DownloadContainer cloudflare-warp .  
COPY warp.sh .  
  
RUN chmod +x cloudflare-warp  
RUN chmod +x warp.sh  
  
ENTRYPOINT ["./warp.sh"]  

