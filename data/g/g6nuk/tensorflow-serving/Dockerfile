FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y \  
curl \  
sudo && \  
echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt
stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee
/etc/apt/sources.list.d/tensorflow-serving.list && \  
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-
serving.release.pub.gpg | sudo apt-key add \- && \  
sudo apt-get update && sudo apt-get install tensorflow-model-server=1.5.0 && \  
mkdir /model && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
ADD start.sh .  
RUN chmod +x ./start.sh  
EXPOSE 9000  
CMD ["./start.sh"]  

