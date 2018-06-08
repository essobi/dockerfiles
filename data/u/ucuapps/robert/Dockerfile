FROM ucuapps/robert-base:latest  
  
MAINTAINER "UCU APPS"  
  
LABEL Description="This ROS Kinetic image containes all dependencies for
Robert development with IDEs" Vendor="UCU APPS" Version="1.0"  
  
ENV remote_deploy_script="https://raw.githubusercontent.com/shadow-robot/sr-
build-tools/$toolset_branch/ansible/deploy.sh"  
  
RUN set -x && \  
  
echo "Removing workspace folder" && \  
rm -rf /home/$MY_USERNAME/workspace && \  
  
echo "Installing and compiling source code" && \  
wget -O /tmp/oneliner "$( echo "$remote_deploy_script" | sed 's/#/%23/g' )" &&
\  
chmod 755 /tmp/oneliner && \  
gosu $MY_USERNAME /tmp/oneliner -o ucuapps -r robert -b kinetic-devel -v
kinetic && \  
  
echo "Sourcing workspace in .bashrc" && \  
echo 'source /home/$MY_USERNAME/workspace/robert/base/devel/setup.bash' >>
/home/$MY_USERNAME/.bashrc && \  
  
echo "Removing cache" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /home/$MY_USERNAME/.ansible
/home/$MY_USERNAME/.gitconfig  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["/usr/bin/terminator"]

