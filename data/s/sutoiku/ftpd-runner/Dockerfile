FROM mhart/alpine-node  
  
COPY cli.js index.js package.json proftpd.conf.tpl docker/* /apps/proftpd-
runner/  
  
RUN apk add --update ncftp gcc make musl-dev perl && \  
addgroup -g 40561 stoic && adduser -u 40561 -G stoic -D stoic && \  
cd /apps/proftpd-runner/ && npm i --production && mkdir default-ftpd && chown
-R stoic:stoic default-ftpd && \  
./install_proftpd.sh && \  
rm -rf proftpd-* && \  
npm uninstall -g npm && \  
apk del --purge gcc make musl-dev && rm -rf /var/cache/apk/*  
  
USER stoic  
  
WORKDIR /apps/proftpd-runner  
  
ENTRYPOINT ["node", "cli"]  
  
# example usage:  
CMD [ "--port=2121", "--users=joe", "--passwds=joe", "--homes=/usr/share/man"]  

