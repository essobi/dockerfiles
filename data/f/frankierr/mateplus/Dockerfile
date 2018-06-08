FROM maven:3-jdk-8  
MAINTAINER Frankie Robertson <frankie@robertson.name>  
  
RUN apt-get update && apt-get install -y \  
git \  
&& apt-get update \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY fetch-drive.sh /usr/bin/  
RUN chmod +x /usr/bin/fetch-drive.sh  
  
RUN git clone https://github.com/microth/PathLSTM.git  
  
COPY fetch-pathlstm-reqs.sh /PathLSTM/scripts/  
COPY parse-pathlstm.sh /PathLSTM/scripts/parse.sh  
RUN chmod +x /PathLSTM/scripts/*.sh  
  
RUN cd PathLSTM && \  
./scripts/fetch-pathlstm-reqs.sh && \  
rm ./scripts/fetch-pathlstm-reqs.sh  
  
RUN cd PathLSTM && mvn compile  
  
CMD cd PathLSTM && \  
cat - > in.txt && \  
./scripts/parse.sh in.txt 1>&2 && \  
cat out.txt && \  
rm in.txt out.txt  

