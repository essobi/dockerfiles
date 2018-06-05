FROM beevelop/java  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
ENV PATH=$PATH:/opt/sonar/bin \  
SONARLINT_VERSION="2.1.0.566"  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y unzip && \  
wget --quiet "https://sonarsource.bintray.com/Distribution/sonarlint-
cli/sonarlint-cli-${SONARLINT_VERSION}.zip" -O sonarlint.zip && \  
unzip sonarlint && \  
mv sonarlint-* sonar && \  
rm sonarlint.zip && \  
mkdir /code /report  
  
WORKDIR /code  
  
CMD sonarlint --html-report /report/sonar.html  

