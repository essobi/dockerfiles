FROM centos  
ARG OPT_DIR=/opt/rendertron  
RUN mkdir -p $OPT_DIR  
WORKDIR $OPT_DIR  
RUN yum install -y epel-release && \  
yum install -y git curl && \  
curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \  
yum -y install nodejs && \  
echo -e "\  
[google-chrome] \n\  
name=google-chrome \n\  
baseurl=https://dl.google.com/linux/chrome/rpm/stable/\$basearch \n\  
enabled=1 \n\  
gpgcheck=1 \n\  
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub \n\  
" > /etc/yum.repos.d/google-chrome.repo && \  
cat /etc/yum.repos.d/google-chrome.repo && \  
yum install -y google-chrome-stable  
  
RUN cd /opt && \  
git clone https://github.com/GoogleChrome/rendertron.git && \  
cd rendertron && \  
npm install  
EXPOSE 3000  
ENTRYPOINT ["npm", "run", "start"]  

