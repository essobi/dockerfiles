FROM ubuntu  
COPY sources.list /etc/apt/sources.list  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get dist-upgrade  
RUN apt-get autoremove  
RUN apt-get autoclean  
RUN apt-get install -y default-jre  
RUN apt-get install -y default-jdk  
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/
wheezy main" | tee /etc/apt/sources.list.d/azure-cli.list  
RUN apt-key adv --keyserver packages.microsoft.com --recv-keys 417A0893  
RUN apt-get install -y apt-transport-https  
RUN apt-get update && apt-get install azure-cli  
RUN apt install -y docker.io  
RUN sed -i -e 's/us.archive.ubuntu.com/archive.ubuntu.com/g'
/etc/apt/sources.list  
RUN apt-get update && apt-get install curl  
RUN apt-get -y install maven  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
RUN ssh-keygen -f id_rsa -t rsa -N ''  

