FROM alpine:latest  
MAINTAINER playniuniu@gmail.com  
  
ENV C_FORCE_ROOT="true" \  
INSTALL_PKG="python py-virtualenv git ansible openssh-client sshpass rsync"  
COPY app /usr/src/app/  
COPY config /root/config/  
  
WORKDIR /usr/src/app  
  
RUN apk add --no-cache --update ${INSTALL_PKG} \  
&& virtualenv /env \  
&& /env/bin/pip install --no-cache-dir -r /root/config/requirements.txt \  
&& rm -rf /var/cache/apk/* \  
&& chmod +x /usr/src/app/inventory.py  
  
VOLUME /data  
EXPOSE 8000  
ENTRYPOINT ["/root/config/entrypoint.sh"]  
CMD ["/env/bin/gunicorn", "-b", "0.0.0.0:8000", "flansible:app"]  

