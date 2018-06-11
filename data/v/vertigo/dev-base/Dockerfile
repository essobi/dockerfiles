# Base CentOS 7 with dev tools  
  
FROM vertigo/java8:latest  
  
MAINTAINER Rubens Neto <rubens@vertigo.com.br>  
  
ARG BASEREPO  
ARG EPELREPO  
  
RUN sh /opt/setbaserepo.sh && \  
sh /opt/setepelrepo.sh && \  
yum -y groupinstall "Development Tools" && \  
yum install ansible zsh autojump fasd docker -y && \  
yum clean all  
  
# Install Zsh  
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh && \  
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc && \  
chsh -s /bin/zsh && \  
sed "s/^plugins.*/plugins=(git docker encode64 fasd jsontools urltools history
autojump wd)/" -i ~/.zshrc  
RUN sh -c "$(curl -sL https://download.getcarina.com/dvm/latest/install.sh)"
&& \  
echo "source ~/.dvm/dvm.sh" >> /root/.bashrc && \  
echo "source ~/.dvm/dvm.sh" >> /root/.zshrc && \  
source /root/.dvm/dvm.sh && \  
dvm list && \  
curl -sL https://download.getcarina.com/carina/latest/$(uname -s)/$(uname
-m)/carina -o carina && \  
mkdir -p ~/bin && \  
mv carina ~/bin/carina && \  
chmod u+x ~/bin/carina && \  
echo 'export PATH=~/bin:$PATH' >> /root/.bashrc && \  
echo 'export PATH=~/bin:$PATH' >> /root/.zshrc  
#RUN useradd developer  
#USER developer  
#RUN git config --global user.name "Vertigo Developer" && \  
# git config --global user.email "developer@vertigo.com.br"  
#ADD src/* /opt/  
#USER developer  

