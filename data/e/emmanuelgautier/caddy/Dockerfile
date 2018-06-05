FROM alpine  
  
LABEL maintainer "Emmanuel Gautier <docker@emmanuelgautier.fr>"  
  
COPY \--from=emmanuelgautier/caddy:builder /install/caddy /usr/bin/caddy  
COPY Caddyfile /etc/Caddyfile  
  
VOLUME /root/.caddy  
  
EXPOSE 80 443 2015  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  

