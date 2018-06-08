FROM debian:9.2  
RUN apt-get update  
RUN apt-get install -y wget dos2unix nginx openssh-server createrepo rpm tar
gnupg sudo cron rsync  
RUN apt-get upgrade -y  
RUN apt-get autoremove  
RUN apt-get clean  
  
ENV ARCHITECTURE="x86_64"  
ENV VERSION="5.11"  
ENV REPO_PASSWD="123456"  
ENV REPO_ADDRESS="http://127.0.0.1"  
ENV REPO_NAME="myrepo"  
ENV GPG_NAME="John Doe"  
ENV GPG_EMAIL="localhost@localhost"  
COPY ./tools/sync-repo /usr/local/bin/sync-repo  
RUN dos2unix /usr/local/bin/sync-repo \  
&& chmod +x /usr/local/bin/sync-repo  
  
COPY ./tools/start-packages /usr/local/bin/start-packages  
RUN dos2unix /usr/local/bin/start-packages \  
&& chmod +x /usr/local/bin/start-packages  
  
COPY ./tools/create-repo /usr/local/bin/create-repo  
RUN dos2unix /usr/local/bin/create-repo \  
&& chmod +x /usr/local/bin/create-repo  
  
COPY ./tools/create-gpg /usr/local/bin/create-gpg  
RUN dos2unix /usr/local/bin/create-gpg \  
&& chmod +x /usr/local/bin/create-gpg  
  
COPY ./nginx/centos /etc/nginx/sites-available/default  
  
RUN mkdir -p /etc/i9corp/packages  
  
RUN useradd -ms /bin/bash repo  
RUN chown -R repo:repo /etc/i9corp/packages  
RUN echo 'repo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# CRON EM SILENT MODE  
# RUN echo "*/30 * * * * root /usr/bin/nohup sudo /usr/local/bin/sync-repo
>/dev/null 2>&1 &" >> /usr/src/cron.tmp  
# RUN echo "" >> /usr/src/cron.tmp \  
# && crontab /usr/src/cron.tmp \  
# && rm /usr/src/cron.tmp  
WORKDIR /etc/i9corp/packages  
  
RUN mkdir -p ~/.ssh \  
&& touch ~/.ssh/authorized_keys \  
&& chmod 644 ~/.ssh/authorized_keys  
  
VOLUME [ "/etc/i9corp/packages" ]  
  
#Nginx  
EXPOSE 80  
#SSH  
EXPOSE 22  
CMD ["/usr/local/bin/start-packages"]  

