FROM ubuntu:xenial  
LABEL Anatoly_Litovsky=<anatolylit@gmail.com>  
LABEL Yair_Zaslavsky=<yair.zaslavsky@gmail.com>  
ENV container docker  
#TODO : make it auto detectable from inside  
ENV LOCAL_SOCKET_DIR /sockets  
  
RUN apt-get clean && apt-get update  
RUN apt-get install -y apt-utils nginx python git python3-pip python3-openssl
gettext-base  
  
RUN pip3 install pip --upgrade && pip3 install ipdb flask flask_httpauth
docker-py jinja2  
  
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
  
#turn this delete and copy into patch applying  
COPY keys /root/keys  
RUN chmod 600 /root/keys/*  
RUN chmod 600 /root/keys  
RUN cd /var/www/html; env GIT_SSH_COMMAND='ssh -i /root/keys/deploykey -o
"UserKnownHostsFile /root/keys/known_hosts"' git clone
git@bitbucket.org:cloudpurge/novnc.git novnc  
RUN cd /var/www/html/novnc; git checkout master  
RUN cd /var/www/html; env GIT_SSH_COMMAND='ssh -i /root/keys/deploykey -o
"UserKnownHostsFile /root/keys/known_hosts"' git clone
git@bitbucket.org:cloudpurge/spice-html5.git spice  
RUN cd /var/www/html/spice; git checkout master  
RUN cd /var/www/html; env GIT_SSH_COMMAND='ssh -i /root/keys/deploykey -o
"UserKnownHostsFile /root/keys/known_hosts"' git clone
git@bitbucket.org:cloudpurge/mainpage.git  
RUN cd /var/www/html/mainpage; git checkout master  
RUN rm -rf /root/keys  
  
#lets make the main pages  
RUN cd /var/www/html/mainpage && /bin/bash -c "source gen_pages.sh"  
RUN rm -rf /var/www/html/mainpage  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/default /etc/nginx/sites-enabled/default  
  
#add the dispatcher server  
RUN pwd  
COPY dispatcher /dispatcher  
RUN python3 -m compileall -l -f -b dispatcher  
RUN rm -rf /dispatcher/*.py  
  
RUN mkdir -p /mnt/locks  
RUN chmod 777 /mnt/locks  
VOLUME /mnt/locks  
  
RUN mkdir /certs  
  
EXPOSE 8888  
EXPOSE 443  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
ENV CERT /certs/cert.pem  
ENV KEY /certs/key.pem  
  
CMD ["/run.sh"]  
  
#mkf=dir - name: Making dispatcher container  
#mkf=dir docker_container:  
#mkf=dir name: dispatcher  
#mkf=dir image: cloudpurge/cagefox-dispatcher:{{dispatcher_tag}}  
#mkf=dir state: present  
#mkf=dir volumes:  
#mkf=dir - "/var/run/docker.sock:/var/run/docker.sock"  
#mkf=dir - "/etc/letsencrypt/live/{{ inventory_hostname
}}/fullchain.pem:/certs/cert.pem"  
#mkf=dir - "/etc/letsencrypt/live/{{ inventory_hostname
}}/privkey.pem:/certs/key.pem"  
#mkf=dir - "/mnt/users:/mnt/users"  
#mkf=dir volumes_from:  
#mkf=dir - sockets_share  
#mkf=dir ports:  
#mkf=dir - "8080:8080"  
#mkf=dir - "443:443"  
#mkf=dir env:  
#mkf=dir DISPATCHER_CONTAINER: dispatcher  
#mkf=dir SOCKETS_SHARE: sockets_share  
#mkf=dir HOST_USER_MOUNT: /mnt/users  

