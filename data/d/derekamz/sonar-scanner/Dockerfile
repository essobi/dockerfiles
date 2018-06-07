FROM openjdk:8-alpine  
ENV SONAR_SCANNER_VERSION 2.8  
RUN apk update && apk add --no-cache wget python perl valgrind && \  
wget --no-check-certificate
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-${SONAR_SCANNER_VERSION}.zip && \  
unzip sonar-scanner-${SONAR_SCANNER_VERSION} && \  
cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner
sonar-scanner && \  
apk del wget  
  
COPY cppcheck /usr/bin/cppcheck  
  
# cpplint  
# python /cpplint_mod.py source.cpp 2> report.txt  
# perl /cpplintReport2checkstyleReport.perl report.txt splint-result-0.xml  
COPY cpplint_mod.py /cpplint_mod.py  
COPY cpplintReport2checkstyleReport.perl /cpplintReport2checkstyleReport.perl  
  
COPY ./cfg /usr/bin/  
  
RUN chmod +x /usr/bin/cppcheck  
  
COPY run-scanner.sh /usr/bin/run-scanner.sh

