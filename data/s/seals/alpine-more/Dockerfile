FROM alpine:latest  
  
ARG fdupesver=1.6.1  
RUN apk update && \  
apk --no-cache upgrade && \  
apk --no-cache add bash ncdu nano dropbear mc python3 git alpine-sdk screen
tmux  
  
#add fdupes from source, since there isn't an Alpine package available  
ADD https://github.com/adrianlopezroche/fdupes/archive/v${fdupesver}.tar.gz
/tmp/fdupes/src.tar.gz  
WORKDIR /tmp/fdupes  
RUN tar -xvf src.tar.gz  
WORKDIR /tmp/fdupes/fdupes-${fdupesver}  
RUN make fdupes && \  
make install && \  
rm -rf /tmp/fdupes  
WORKDIR /  
  
# remove unneeded SDK, since we are done building fdupes  
RUN apk --no-cache del alpine-sdk  
  
#Install pip for python  
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py  
RUN python3 /tmp/get-pip.py && \  
rm /tmp/get-pip.py && \  
pip3 install setuptools --upgrade && \  
pip3 install wheel --upgrade  
  
#add alias  
RUN echo 'alias ll="ls -la"' > /root/.bashrc && \  
echo 'alias fd="fdupes -r -A -S -d \$(pwd)"' >> /root/.bashrc && \  
echo 'alias fdt="fdupes -r -A \$(pwd)"' /root/.bashrc && \  
chmod 600 /root/.bashrc  
  
#add .profile so .bashrc is used  
RUN echo "# ~/.profile: executed by the command interpreter for login shells."
> /root/.profile && \  
echo "# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login"
>> /root/.profile && \  
echo "# exists." >> /root/.profile && \  
echo "# see /usr/share/doc/bash/examples/startup-files for examples." >>
/root/.profile && \  
echo "# the files are located in the bash-doc package." >> /root/.profile && \  
echo "" >> /root/.profile && \  
echo "# the default umask is set in /etc/profile; for setting the umask" >>
/root/.profile && \  
echo "# for ssh logins, install and configure the libpam-umask package." >>
/root/.profile && \  
echo "#umask 022" >> /root/.profile && \  
echo "" >> /root/.profile && \  
echo "# if running bash" >> /root/.profile && \  
echo "if [ -n \"\$BASH_VERSION\" ]; then" >> /root/.profile && \  
echo " # include .bashrc if it exists" >> /root/.profile && \  
echo " if [ -f \"\$HOME/.bashrc\" ]; then" >> /root/.profile && \  
echo " . \"\$HOME/.bashrc\"" >> /root/.profile && \  
echo " fi" >> /root/.profile && \  
echo "fi" >> /root/.profile && \  
echo "" >> /root/.profile && \  
echo "# set PATH so it includes user's private bin if it exists" >>
/root/.profile && \  
echo "if [ -d \"\$HOME/bin\" ] ; then" >> /root/.profile && \  
echo " PATH=\"\$HOME/bin:\$PATH\"" >> /root/.profile && \  
echo "fi" >> /root/.profile && \  
echo "" >> /root/.profile && \  
#echo "# run tumx by default to allow disconnect\reconnect" >> /root/.profile
&& \  
#echo "tmux" >> /root/.profile && \  
chmod 600 /root/.profile  
  
#set password for root user so you can ssh, set bash as default shell  
RUN sed -i 's~/bin/ash~/bin/bash~' /etc/passwd && \  
echo 'root:password' | chpasswd  
  
#Create required folder for dropbear  
RUN mkdir -p /etc/dropbear/  
  
#expose the ssh port  
EXPOSE 32768  
#run dropbear sshd server  
CMD ["/usr/sbin/dropbear", "-R", "-E", "-F", "-a", "-p", "32768", "-K", "30"]  

