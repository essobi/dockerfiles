#  
# optimizationbenchmarking/evaluator-gui  
#  
# This is the image of the graphical user interface of our  
# evaluator.  
#  
FROM optimizationbenchmarking/evaluator-runtime:0.8.6  
MAINTAINER Thomas Weise <tweise@ustc.edu.cn>  
  
RUN export LANG=C.UTF-8 &&\  
apt-get update &&\  
apt-get install -f -y wget &&\  
cd /usr/local/bin/ &&\  
wget https://github.com/optimizationBenchmarking/evaluator-
gui/releases/download/0.8.9/evaluatorGui.jar &&\  
chmod +x /usr/local/bin/evaluatorGui.jar &&\  
mkdir /data/ &&\  
apt-get purge -f -y wget &&\  
apt-get clean &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*  
  
EXPOSE 8080  
VOLUME /data  
WORKDIR /usr/local/bin/  
  
ENTRYPOINT ["java", "-jar", "/usr/local/bin/evaluatorGui.jar",
"dontOpenBrowser", "rootPath=/data", "port=8080"]

