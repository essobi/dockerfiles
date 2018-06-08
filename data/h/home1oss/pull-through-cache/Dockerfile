  
FROM registry:2.6.1  
# curl -Ls
https://github.com/maxcnunes/waitforit/releases/download/v1.4.0/waitforit-
linux_amd64 >> /usr/bin/waitforit && \  
RUN apk add --no-cache aria2 curl privoxy socat && \  
aria2c --file-allocation=none -c -x 10 -s 10 -m 0 --console-log-level=notice
--log-level=notice --summary-interval=0 -d /usr/bin -o waitforit
https://github.com/maxcnunes/waitforit/releases/download/v1.4.0/waitforit-
linux_amd64 && \  
chmod 755 /usr/bin/waitforit  
  
COPY ./docker/config-example.yml /etc/docker/registry/config-example.yml  
COPY ./docker/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/etc/docker/registry/config.yml"]  

