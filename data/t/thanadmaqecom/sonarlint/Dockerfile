FROM java  
  
ENV PATH=$PATH:/opt/sonar/bin \  
SONARLINT_VERSION="2.1.0.566"  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y unzip && \  
wget --quiet "https://sonarsource.bintray.com/Distribution/sonarlint-
cli/sonarlint-cli-${SONARLINT_VERSION}.zip" -O sonarlint.zip && \  
unzip sonarlint && \  
mv sonarlint-* sonar && \  
rm sonarlint.zip && \  
mkdir /code  
  
VOLUME ["/code"]  
  
WORKDIR /code  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

