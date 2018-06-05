# Base image  
FROM ubuntu:16.04  
# Author's information  
MAINTAINER AnanasYuu <yuyihuang0702@163.com>  
  
# Install dependencies and Create source folders  
RUN apt-get update && apt-get install \--yes \  
bash-completion apt-utils iputils-ping vim wget git-core tzdata \  
python python-pip python-dev && \  
pip install \--upgrade pip && \  
echo "Asia/Shanghai" > /etc/timezone && \  
echo "export TZ='Asia/Shanghai'" >> /etc/bash.bashrc && \  
sed -i "32,38s/^#//g" /etc/bash.bashrc && \  
mkdir -p /home/rally/source  
# Install and configuration Rally  
RUN wget -P /home/rally/
https://raw.githubusercontent.com/openstack/rally/0.12.1/install_rally.sh && \  
sed -i 's/^RALLY_GIT_BRANCH=.*/RALLY_GIT_BRANCH="0.12.1"/'
/home/rally/install_rally.sh && \  
sed -i 's/^RALLY_DATABASE_DIR=.*/RALLY_DATABASE_DIR=\/home\/rally\/data/'
/home/rally/install_rally.sh && \  
sed -i 's/SOURCEDIR="\$ORIG_WD".*/SOURCEDIR="\$ORIG_WD"\/home\/rally\/source/'
/home/rally/install_rally.sh && \  
echo 'cp $SOURCEDIR/etc/motd /etc/motd' >> /home/rally/install_rally.sh && \  
echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/motd' >> /etc/bash.bashrc
&& \  
echo 'source /usr/local/etc/bash_completion.d/rally.bash_completion' >>
/etc/bash.bashrc && \  
bash /home/rally/install_rally.sh && \  
sed -i
"s/ajax.googleapis.com\/ajax\/libs\/angularjs/cdnjs.cloudflare.com\/ajax\/libs\/angular.js/"
\  
/usr/local/lib/python2.7/dist-packages/rally/ui/templates/task/report.html &&
\  
sed -i
"s/ajax.googleapis.com\/ajax\/libs\/angularjs/cdnjs.cloudflare.com\/ajax\/libs\/angular.js/"
\  
/usr/local/lib/python2.7/dist-packages/rally/ui/templates/task/trends.html &&
\  
sed -i
"s/ajax.googleapis.com\/ajax\/libs\/angularjs/cdnjs.cloudflare.com\/ajax\/libs\/angular.js/"
\  
/usr/local/lib/python2.7/dist-
packages/rally/ui/templates/verification/report.html  
# Copy script  
COPY . /home/rally/  
# Cleanup cache  
RUN apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /root/.cache/  
# Recreate rally database  
RUN mkdir -p /home/rally/data && \  
rally db recreate  
  
# Changing workdir  
WORKDIR /home/rally  
# Docker volumes have specific behavior that allows this construction to work.  
# Data generated during the image creation is copied to volume only when it's  
# attached for the first time (volume initialization)  
VOLUME ["/home/rally"]  
  
# Set default command  
CMD ["/bin/bash"]  

