FROM ubuntu:16.04  
  
  
RUN echo "lol" && apt-get update && apt-get install -y wget && apt-get install
-y unzip  
#RUN apt-get install -y mysql-server  
RUN apt-get install -y libmysqlclient-dev  
#RUN apt-get install -y libmariadbclient-dev  
RUN sed -i -e 's/:\/\/(archive.ubuntu.com\|security.ubuntu.com)/old-
releases.ubuntu.com/g' /etc/apt/sources.list  
#WORKDIR sonarlint-cli-2.1.0.566  
RUN apt-get install -y sloccount  
RUN apt-get install -y git  
RUN apt-get install -y python && apt-get install -y python-pip  
#COPY analyse.sh .  
#COPY requirements.txt .  
#COPY static_analysis.py .  
#COPY sonarlint_parse.py .  
#COPY sloccount_parse.py .  
#COPY generate.py .  
#RUN pip install -r requirements.txt  
# run python pop from sqs  
#RUN ./sonarlint-cli-2.1.0.566/bin/sonarlint -h  
#RUN wget https://github.com/lambduh/lambduh-execute/archive/master.zip &&
unzip master.zip  
#RUN wget https://github.com/lambduh/lambduh-execute/archive/master.zip &&
unzip master.zip  
RUN git clone https://github.com/scikit-learn/scikit-learn.git  
#RUN ./bin/sonarlint lambduh-execute-master  
RUN sloccount scikit-learn  
#RUN while sleep 1; do echo "Hi"; done  
#RUN while sleep 1; do python static_analysis.py; done  
#RUN python static_analysis.py  
# python parse sonarlint reports  
# run python upload all of them  

