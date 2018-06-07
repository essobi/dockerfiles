FROM babim/alpinebase:cron.ssh  
  
# install  
RUN apk add --no-cache python py-pip curl bash nano \  
python-dev git gcc musl-dev linux-headers augeas-dev openssl-dev libffi-dev
ca-certificates dialog \  
&& pip install -U letsencrypt \  
&& apk del python-dev git gcc musl-dev linux-headers augeas-dev openssl-dev
libffi-dev ca-certificates dialog  
  
# make data  
ADD run.sh /run.sh  
RUN rm -rf /etc/letsencrypt && mkdir -p /letsencrypt-start/etc && \  
ln -sf /letsencrypt/etc /etc/letsencrypt && chmod +x /run.sh  
  
# make update file  
COPY sh /letsencrypt-start/  
RUN chmod +x /letsencrypt-start/*.sh  
  
VOLUME /letsencrypt/  
WORKDIR /letsencrypt  
ENTRYPOINT ["/run.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  
EXPOSE 80 443  

