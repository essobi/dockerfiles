FROM debian  
ADD https://bin.equinox.io/c/2ovkwS9YHaP/edgetunnels-stable-linux-amd64.tgz .  
RUN tar xzf *.tgz  
  
FROM debian  
COPY \--from=0 cloudflare-warp /usr/local/bin/  
COPY docker-entrypoint.sh /usr/local/bin/  
USER daemon  
ENV ORIGIN_CERT=/run/secrets/cloudflare-warp.pem  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["cloudflare-warp"]  

