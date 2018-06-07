FROM debian:stretch  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install prereqs  
RUN (apt-get update &&\  
apt-get install -y jq python2.7-minimal wget &&\  
rm -rf /var/lib/apt/lists/*)  
  
# install dropbox  
RUN (mkdir /opt/dropbox &&\  
cd /opt/dropbox &&\  
wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -)  
  
# install dropbox.py  
RUN (wget -O /usr/local/bin/dropbox.py
"https://www.dropbox.com/download?dl=packages/dropbox.py" &&\  
chmod +x /usr/local/bin/dropbox.py &&\  
ln -s /usr/bin/python2.7 /usr/bin/python)  
  
# install tini  
RUN (TINI_VER="$(wget -q -O -
https://api.github.com/repos/krallin/tini/releases/latest | jq -r .tag_name)"
&&\  
wget "https://github.com/krallin/tini/releases/download/${TINI_VER}/tini-
amd64" -O /tini &&\  
chmod +x /tini)  
  
# install gosu  
RUN (wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" &&\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc" &&\  
chmod +x /usr/local/bin/gosu)  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/tini","-s","--","dropbox.py","start"]  

