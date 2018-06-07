FROM ubuntu:latest  
MAINTAINER Jake Holland <jholland@akamai.com>  
  
# multi-stage build --jake 2018-04-02  
# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-
stage-builds  
# stage 0  
RUN apt-get update && apt-get install -y build-essential git automake  
  
RUN git clone https://github.com/GrumpyOldTroll/iperf-ssm && \  
cd iperf-ssm && ./configure && make  
  
# stage 1  
FROM ubuntu:latest  
COPY \--from=0 /iperf-ssm/src/iperf /bin/iperf  
ENTRYPOINT ["/bin/iperf"]  
  

