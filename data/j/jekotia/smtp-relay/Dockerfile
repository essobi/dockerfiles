## Derived from https://github.com/namshi/docker-smtp  
FROM jekotia/resin-raspberrypi3-debian  
  
RUN [ "cross-build-start" ]  
###  
##  
#  
RUN apt-get update \  
&& apt-get install -y exim4-daemon-light \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& find /var/log -type f | while read f; do echo -ne '' > $f; done;  
  
#RUN ln -sf /dev/stdout /var/log/exim4/mainlog \  
# && chown 105:111 /var/log/exim4/mainlog  
COPY copy/entrypoint.sh /bin/  
COPY copy/set-exim4-update-conf /bin/  
  
RUN chmod a+x /bin/entrypoint.sh \  
&& chmod a+x /bin/set-exim4-update-conf  
  
#  
##  
###  
RUN [ "cross-build-end" ]  
  
EXPOSE 25  
ENTRYPOINT ["/bin/entrypoint.sh"]  
CMD ["exim", "-bd", "-q15m", "-v"]  
  

