FROM danielguerra/alpine-sshdx  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk --update --no-cache add mono libgdiplus-dev gtk+2.0 ca-certificates
bash\  
&& rm -rf /tmp/* /var/cache/apk/*  
RUN wget http://ericlawrence.com/dl/MonoFiddler-v4484.zip -O fiddler.zip  
RUN unzip fiddler.zip \  
&& rm fiddler.zip  
RUN /usr/bin/cert-sync /etc/ssl/certs/ca-certificates.crt  
RUN /usr/bin/mozroots --sync  
EXPOSE 8888  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["/usr/sbin/sshd","-D"]  

