FROM ubuntu:16.04  
  
ENV SONAR_SCANNER_VERSION 3.1.0.1141  
# Sonar scanner  
  
RUN apt-get update -q && \  
apt-get install -y -q \  
wget \  
unzip \  
git \  
gcc \  
g++ \  
python \  
build-essential \  
cmake \  
cppcheck \  
lcov \  
gcovr \  
valgrind \  
libexpat1-dev \  
vera++ \  
openjdk-8-jre-headless && \  
wget -q https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \  
unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip && \  
cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}-linux/bin/sonar-
scanner sonar-scanner && \  
ln -s /usr/bin/sonar-scanner-run.sh /bin/gitlab-sonar-scanner && \  
git clone https://github.com/andrew-d/rough-auditing-tool-for-security.git
rats && \  
cd rats && \  
./configure && \  
make && \  
make install && \  
cd .. && \  
rm -rf rats && \  
apt-get remove --purge -y -q wget unzip && \  
apt-get autoremove -y -q && \  
rm -rf /var/lib/apt/lists/*  
  
COPY sonar-scanner-run.sh /usr/bin  

