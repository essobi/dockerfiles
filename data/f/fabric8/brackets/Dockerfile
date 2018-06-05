FROM node  
  
RUN npm install brackets -g  
  
# latest version is actually 0.14.22  
  
RUN apt-get -y update && \  
apt-get -y install git unzip && \  
mkdir /var/projects && \  
mkdir -p /var/brackets/extensions/user/zaggino.brackets-git && \  
cd /var/brackets/extensions/user/zaggino.brackets-git && \  
curl -o /tmp/brackets.zip
https://s3.amazonaws.com/extend.brackets/zaggino.brackets-
git/zaggino.brackets-git-0.14.9.zip && \  
unzip /tmp/brackets.zip && \  
rm /tmp/brackets.zip && \  
mkdir -p /support/extensions/user/zaggino.brackets-git  
  
EXPOSE 80  
  
CMD ["brackets", "--port", "80", "--proj-dir", "/var/projects", "--supp-dir",
"/var/brackets", "-d"]  

