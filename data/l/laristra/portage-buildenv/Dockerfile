FROM ubuntu:latest  
#to run this script: docker build -t docker-portage .  
#to start the container: docker run -h simpleportage -it -v /Users:/Users --rm
docker-portage  
#to run as root in it: docker ls; docker exec -itu root <id> bash  
RUN apt-get update && apt-get install -y \  
cmake \  
libopenmpi-dev openmpi-bin \  
libboost-dev \  
liblapack-dev liblapacke-dev \  
python-pip git \  
wget curl lcov doxygen \  
ccache texlive-latex-base texlive-fonts-recommended texlive-latex-recommended
texlive-font-utils \  
g++  
  
RUN apt-get install -y openjdk-8-jdk unzip  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip https://sonarqube.com/static/cpp/build-wrapper-linux-x86.zip  
RUN unzip sonar-scanner-2.8.zip -d /sonarqube/  
RUN unzip build-wrapper-linux-x86.zip -d /sonarqube/  
ENV PATH=${PATH}${PATH:+:}/sonarqube/build-wrapper-linux-x86:/sonarqube/sonar-
scanner-2.8/bin  
RUN sonar-scanner -h  
  
RUN groupadd -r portage  
RUN useradd -r -m -g portage portage  
USER portage  
ENV PATH=/usr/lib/ccache:${PATH}  
WORKDIR /home/portage  
RUN pip install --user codecov coverxygen  
  

