FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
  
ENV GIT_USERNAME HongshunYang  
ENV GIT_EMAIL yanghongshun@outlook.com  
  
RUN apk -U add git abuild \  
&& adduser -G abuild -g "Alpine Package Builder" -s /bin/sh -D builder \  
&& echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& rm -rf /var/cache/apk/*  
  
COPY rootfs/usr_local_bin_abuild-keygen-run /usr/local/bin/abuild-keygen-run  
RUN chmod a+x /usr/local/bin/*  
  
RUN chown -R builder /home/builder \  
&&mkdir -p /keys \  
&&chown -R builder /keys  
  
VOLUME /keys  
  
USER builder  
  
CMD ["abuild-keygen-run"]  
  

