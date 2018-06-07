##gitcloneして、setup.rb呼ぶ  
#docker run --rm -it -e REPO=git@github.com:**.git -e REPO_DIR=** -v
~/:/keyfolder -v /var/run/docker.sock:/var/run/docker.sock sato0203/docker-
provisioner  
#base OS  
FROM ubuntu:16.04  
# before setup  
RUN apt update -y && \  
apt upgrade -y && \  
apt install docker -y && \  
apt install docker-compose -y && \  
apt install git -y  
  
# setup ruby  
RUN apt update -y && \  
apt upgrade -y && \  
apt install -y rbenv ruby-build ruby-dev sudo && \  
echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc && \  
. $HOME/.bashrc && \  
hash -r && \  
rbenv install 2.2.3 && \  
rbenv global 2.2.3  
#gitclone and provisioning  
CMD cd /keyfolder && \  
mkdir /root/.ssh && \  
cp deploykey ~/.ssh/id_rsa && \  
echo "Host github.com" >> ~/.ssh/config && \  
echo " " >> ~/.ssh/config && \  
echo "StrictHostKeyChecking no" >> ~/.ssh/config && \  
mkdir /gitfolder && \  
cd /gitfolder && \  
git clone $REPO && \  
cd $REPO_DIR && \  
ruby setup.rb && \  
exit

