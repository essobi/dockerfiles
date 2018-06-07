From ubuntu:latest  
  
ENV SONAR_SCANNER_VERSION 2.8  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y gnupg2  
RUN apt-get install -y apt-utils  
RUN apt-get install -y git sudo make locate wget ruby-dev host gem
bsdmainutils  
RUN /bin/bash -c "wget
sourceforge.net/projects/ubuntuzilla/files/mozilla/apt/pool/main/f/firefox-
mozilla-build/firefox-mozilla-build_39.0.3-0ubuntu1_amd64.deb;dpkg -i firefox-
mozilla-build_39.0.3-0ubuntu1_amd64.deb"  
RUN apt-get install -y python-setuptools python-dev build-essential  
RUN apt-get install -y npm  
RUN apt-get install -y maven  
RUN apt-get install -y xvfb  
RUN apt-get install -y python-cffi  
RUN apt-get -y upgrade  
RUN npm install -g eslint  
RUN npm install -g retire  
RUN npm install -g eslint-plugin-scanjs-rules  
RUN npm install -g eslint-plugin-no-unsafe-innerhtml  
  
RUN easy_install pip  
RUN pip install datadog  
RUN pip install sslyze  
RUN git clone https://github.com/18F/compliance-toolkit.git /opt/compliance-
toolkit  
RUN git clone https://github.com/ToddBenson/concourse-maven-spring-boot
/opt/base-project  
RUN git clone https://github.com/gauntlt/gauntlt /opt/gauntlt  
RUN git clone https://github.com/drwetter/testssl.sh.git /opt/testssl  
  
RUN /bin/bash -c "cd /opt/gauntlt; source ./install_gauntlt_deps.sh"; exit 0  
RUN bash /opt/gauntlt/ready_to_rumble.sh  
RUN pip uninstall cryptography -y  
RUN pip install cryptography  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN cd /opt/base-project;./mvnw clean install  
ADD "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-${SONAR_SCANNER_VERSION}.zip" /  
RUN unzip "sonar-scanner-${SONAR_SCANNER_VERSION}.zip"  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
ENV PATH=/sonar-scanner-${SONAR_SCANNER_VERSION}/bin:/bin:${PATH}  
  
#From ubuntu:latest  
#RUN apt-get update  
#RUN apt-get install -y git sudo make locate wget ruby-dev host gem
bsdmainutils|| true  
#RUN git clone https://github.com/gauntlt/gauntlt /opt/gauntlt  
#RUN git clone https://github.com/drwetter/testssl.sh.git /opt/testssl  
#RUN /bin/bash -c "cd /opt/gauntlt; source ./install_gauntlt_deps.sh"; exit 0  
#RUN bash /opt/gauntlt/ready_to_rumble.sh  
#RUN pip install datadog  

