From alpine:3.4  
EXPOSE 22  
COPY utils /  
RUN apk --update add openssh \  
&& apk add sshpass \  
&& rm -rf /var/cache/apk/* \  
&& chmod -R +x /bkpmikrotik/* \  
&& mkdir /bkpmikrotik/files  
CMD ["/bkpmikrotik/start.sh"]  

