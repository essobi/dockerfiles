FROM ubuntu:latest  
RUN apt-get -q update -y  
RUN apt-get -qq install -y make cmake cmake-data git g++ gfortran flex doxygen
graphviz pandoc python2.7 libopenmpi-dev libcereal-dev liblapacke-dev
libexodusii-dev libscotch-dev libmetis-dev python-pip texlive-font-utils clang
llvm ccache texlive-latex-base texlive-fonts-recommended texlive-latex-
recommended gdb wget curl lcov  
RUN wget -O /usr/bin/doxy-coverage
https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py  
RUN chmod +x /usr/bin/doxy-coverage  
  
RUN apt-get install -y openjdk-8-jdk unzip software-properties-common python-
software-properties  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip https://sonarqube.com/static/cpp/build-wrapper-linux-x86.zip  
RUN unzip sonar-scanner-2.8.zip -d /sonarqube/  
RUN unzip build-wrapper-linux-x86.zip -d /sonarqube/  
ENV PATH=${PATH}${PATH:+:}/sonarqube/build-wrapper-linux-x86:/sonarqube/sonar-
scanner-2.8/bin  
  
RUN groupadd -r user  
RUN useradd -r -m -g user user  
USER user  
ENV PATH=/usr/lib/ccache:${PATH}  
WORKDIR /home/user  
RUN pip install --user codecov coverxygen  

