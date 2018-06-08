FROM debian  
  
RUN \  
build_packages="git scons gcc npm" &&\  
apt-get -qq update &&\  
apt-get install -y $build_packages curl python nodejs-legacy &&\  
git clone https://github.com/armon/statsite.git /usr/src/statsite &&\  
cd /usr/src/statsite &&\  
git checkout 42560e8ca7427171eb5a9dc26e1fc7d648ae5315 &&\  
scons statsite &&\  
cp statsite /usr/local/bin &&\  
mkdir -p /usr/local/lib/statsite &&\  
cp -r sinks /usr/local/lib/statsite &&\  
cd / &&\  
confd_url=https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 &&\  
curl -L "$confd_url" > /usr/local/bin/confd &&\  
chmod a+x /usr/local/bin/confd &&\  
npm install -g git://github.com/ktilcu/statsite-stackdriver &&\  
rm -rf /usr/src/statsite &&\  
apt-get -y purge $build_packages &&\  
apt-get -y autoremove &&\  
apt-get -y clean &&\  
rm -rf /var/lib/apt/lists/*  
  
COPY confd /etc/confd  
COPY compile_and_run.sh /  
  
EXPOSE 8125/udp  
EXPOSE 8125/tcp  
  
ENTRYPOINT ["/compile_and_run.sh"]  
CMD ["/usr/local/bin/statsite", "-f", "/etc/statsite.ini"]  

