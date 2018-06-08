FROM benchflow/base-images:dns-envconsul-java8_dev  
  
MAINTAINER Vincenzo FERME <info@vincenzoferme.it>  
  
ENV TEST_ORCHESTRATOR_VERSION v-dev  
  
# Get benchflow-test-orchestrator  
RUN wget -q --no-check-certificate -O /app/benchflow-test-orchestrator.jar
https://github.com/benchflow/test-
orchestrator/releases/download/$TEST_ORCHESTRATOR_VERSION/benchflow-test-
orchestrator.jar  
  
COPY ./conf/prod.conf /app/  
  
COPY ./services/300-test-orchestrator.conf /apps/chaperone.d/300-test-
orchestrator.conf  
  
EXPOSE 8080

