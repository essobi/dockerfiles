FROM maven:3.3.9-jdk-8  
MAINTAINER Adam Struck <strucka@ohsu.edu>  
  
USER root  
ENV PATH /opt/bin:$PATH  
  
RUN apt-get update && \  
apt-get install --yes \  
build-essential \  
git \  
python \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
RUN git clone https://github.com/PathwayAndDataAnalysis/mutex.git && \  
cd mutex && \  
mvn clean compile && \  
mvn assembly:single && \  
mv target/mutex.jar /opt/  
  
COPY ./mutex.py /opt/bin/  
RUN chmod +x /opt/bin/mutex.py  
ENV PATH=$PATH:/opt/bin/  
  
WORKDIR /home/  
ENTRYPOINT []  
CMD []  

