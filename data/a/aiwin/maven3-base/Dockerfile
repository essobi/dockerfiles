FROM maven:3.3-jdk-8  
LABEL maintainer="javier.boo@aiwin.es"  
  
RUN apt-get update && apt-get install -y jq zip python git  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" && \  
python /tmp/get-pip.py && \  
pip install awscli --ignore-installed six  
  
RUN git clone https://github.com/aiwin-tools/devops-scripts.git
"$HOME/scripts"  
  
ADD settings.xml $MAVEN_CONFIG  

