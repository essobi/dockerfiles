FROM customercentrix/java8  
  
# Thoughtworks Go 14.2 Agent  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
  
RUN date -u +"%Y-%m-%d %H:%M:%S" && apt-get update \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get -y upgrade \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get -y install mysql-client-5.6
phantomjs ant ivy \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get -y install apt-transport-https ca-
certificates lxc iptables \  
&& date -u +"%Y-%m-%d %H:%M:%S" && echo deb https://get.docker.io/ubuntu
docker main > /etc/apt/sources.list.d/docker.list \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 \  
&& date -u +"%Y-%m-%d %H:%M:%S" && curl -sL https://deb.nodesource.com/setup |
sudo bash - \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get update \  
&& date -u +"%Y-%m-%d %H:%M:%S" && apt-get install -y lxc-docker nodejs build-
essential \  
&& date -u +"%Y-%m-%d %H:%M:%S" && wget -O /usr/share/ant/lib/jsch-0.1.51.jar
http://central.maven.org/maven2/com/jcraft/jsch/0.1.51/jsch-0.1.51.jar \  
&& date -u +"%Y-%m-%d %H:%M:%S" && wget -O /tmp/go-agent.deb
http://download.go.cd/gocd-deb/go-agent-14.2.0-377.deb \  
&& date -u +"%Y-%m-%d %H:%M:%S" && dpkg -i /tmp/go-agent.deb \  
&& date -u +"%Y-%m-%d %H:%M:%S" && rm -f /tmp/go-agent.deb \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i '/.*GO_SERVER.*/d' /etc/default/go-
agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i '/.*GO_SERVER_PORT.*/d'
/etc/default/go-agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/DAEMON=Y/DAEMON=N/'
/etc/default/go-agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/su -/su -p/' /etc/init.d/go-agent
\  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/pkill -u go/pkill/'
/etc/init.d/go-agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/pgrep -u go/pgrep/'
/etc/init.d/go-agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/su -p go/su/' /etc/init.d/go-
agent \  
&& date -u +"%Y-%m-%d %H:%M:%S" && chmod +x /usr/local/bin/wrapdocker \  
&& date -u +"%Y-%m-%d %H:%M:%S" && mkdir /scratch \  
&& date -u +"%Y-%m-%d %H:%M:%S"  
  
VOLUME /var/lib/docker  
CMD wrapdocker && /etc/init.d/go-agent start  
  

