FROM java:8  
# install common tools  
# need to get git from unstable to get >= 2.4 which supports --invert-grep;
safety not guaranteed  
RUN echo 'deb http://ftp.us.debian.org/debian unstable main contrib non-free'
>/etc/apt/sources.list.d/unstable.list && \  
apt-get update && \  
apt-get install -y git jq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# according to Brian Clements, can't `git pull` unless we set these  
RUN git config --global user.email "git@localhost" && \  
git config --global user.name "git"  
# install git resource (and disable LFS, which we happen not to need)  
  
RUN mkdir -p /opt/resource/git && \  
wget https://github.com/concourse/git-resource/archive/master.zip -O
/opt/resource/git/git-resource.zip && \  
unzip /opt/resource/git/git-resource.zip -d /opt/resource/git && \  
mv /opt/resource/git/git-resource-master/assets/* /opt/resource/git && \  
rm -r /opt/resource/git/git-resource.zip /opt/resource/git/git-resource-master
&& \  
sed -i '/lfs/s/^/# /' /opt/resource/git/in  
  
# install gradle cache resource  
  
ADD check in out /opt/resource/  
RUN mkdir /var/cache/git  

