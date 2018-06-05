from ubuntu:16.04  
run apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y vim mc git screen wget curl bash-completion npm zip
autoconf libtool mpc \  
apt-transport-https apt-utils ca-certificates software-properties-common \  
mosquitto-clients imagemagick python virtualenv python-pip redis-tools \  
ruby-dev  
  
#SDK  
run pip install --upgrade watson-developer-cloud cloudfoundry-client  
  
#docker  
run curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
run add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
run apt-get update  
run apt-get install -y docker-ce  
  
#cf  
run wget -q -O -
https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key
add -  
run echo "deb http://packages.cloudfoundry.org/debian stable main" | tee
/etc/apt/sources.list.d/cloudfoundry-cli.list  
run apt-get update && apt-get install -y cf-cli  
  
#bx  
run curl https://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-
cli/0.6.6/IBM_Cloud_CLI_0.6.6_amd64.tar.gz | tar xvz  
run Bluemix_CLI/install_bluemix_cli  
run rm -rf Bluemix_CLI  
run bx plugin install container-registry -r Bluemix  
run bx plugin install container-service -r Bluemix  
run bx plugin install cloud-functions -r Bluemix  
run bx plugin install dev -r Bluemix  
run bx plugin install logging-cli -r Bluemix  
  
#kubernetes  
run curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
run chmod +x ./kubectl  
run mv ./kubectl /usr/local/bin/kubectl  
EXPOSE 8001  
#helm  
RUN curl https://storage.googleapis.com/kubernetes-
helm/helm-v2.8.0-rc.1-linux-amd64.tar.gz | tar xvz  
RUN chmod +x linux-amd64/helm  
RUN mv linux-amd64/helm /usr/local/bin/helm  
RUN rm -rf linux-amd64  
  
#istio  
RUN cd /root && curl -L https://git.io/getLatestIstio | sh -  
RUN echo "PATH=\$PATH:/root/istio-0.4.0/bin" >> /root/.bashrc  
  
#wsk  
run wget https://openwhisk.ng.bluemix.net/cli/go/download/linux/amd64/wsk  
run chmod 700 wsk  
run mv wsk /usr/local/bin/  
  
#travis  
run gem install travis  
  
#platformio  
run pip install platformio  
  
#script  
run mkdir /root/bin  
copy init.sh /root/bin/  
copy pushVisualRecognition.sh /root/bin/  
copy clearDomains.py /root/bin/  
copy start_cluster.sh /root/bin/  
  
run echo "PATH=\$PATH:/root/bin/" >> /root/.bashrc  
run echo "echo \" -------> Please run init.sh <\---------\"" >> /root/.bashrc  
  
workdir /root  

