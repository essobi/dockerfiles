FROM geertbongers/home-user  
MAINTAINER Geert  
  
RUN apt-get update && apt-get install -qy --force-yes git-core python python-
cheetah wget  
ADD http://rarlab.com/rar/rarlinux-x64-5.1.1.tar.gz /tmp/unrar.tar.gz  
  
RUN wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py  
RUN apt-get install -qy --reinstall build-essential python-pip python-dev
libssl-dev libffi-dev  
RUN pip2.7 install -U setuptools pip pyasn1 ndg-httpsclient pyopenssl==0.13.1  
  
RUN git clone https://github.com/SiCKRAGETV/SickRage.git /sickrage &&\  
cd /sickrage &&\  
git checkout master &&\  
tar -zxvf /tmp/unrar.tar.gz -C /tmp/ &&\  
cp /tmp/rar/rar /sickrage/lib/unrar2 &&\  
cp /tmp/rar/unrar /sickrage/lib/unrar2 &&\  
ln -s /sickrage/lib/unrar2/rar /usr/bin/rar &&\  
ln -s /sickrage/lib/unrar2/unrar /usr/bin/unrar &&\  
rm -f /tmp/unrar.tar.gz &&\  
rm -Rf /tmp/rar &&\  
mkdir /container-data &&\  
chown -R home_user:home_user /sickrage &&\  
chown -R home_user:home_user /container-data  
  
VOLUME /container-data  
  
EXPOSE 8081  
  
USER home_user  
CMD ["--datadir", "/container-data"]  
ENTRYPOINT ["python", "/sickrage/SickBeard.py"]  

