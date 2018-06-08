FROM ribbituptest/base:1.0  
RUN cd /home && \  
git clone git@bitbucket.org:sgpacific/ribbitup-payment-apps-deployer.git && \  
cd ribbitup-payment-apps-deployer && \  
mvn package -X -e -Dmaven.test.skip=true && \  
cd / && \  
mkdir appsdeployer && \  
cp /home/ribbitup-payment-apps-deployer/target/*.jar
/appsdeployer/appsdeployer.jar && \  
cd /home && \  
rm -rf ribbitup-payment-apps-deployer && \  
apt-get --purge remove -y git maven openjdk-8-jdk-headless && \  
apt-get install -y openjdk-8-jre-headless && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
CMD ["/bin/bash"]  

