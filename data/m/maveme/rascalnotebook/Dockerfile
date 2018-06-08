FROM openjdk:8 as javaEnv  
  
RUN apt-get update \  
&& apt-get install git  
  
WORKDIR /app  
  
RUN git clone https://github.com/maveme/rascal-notebook  
  
RUN apt-get install -y maven  
  
RUN cd rascal-notebook \  
&& mvn clean package  
  
# ------------  
FROM javaEnv as build  
  
RUN apt-get install -y python3-pip  
  
WORKDIR /app  
  
COPY \--from=0 /app/rascal-notebook/src/main/resources/ /app  
  
COPY \--from=0 /app/rascal-notebook/target/rascal-notebook-0.0.1-SNAPSHOT-jar-
with-dependencies.jar /app  
  
####### NODE  
RUN pip3 install --upgrade pip  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
RUN npm install -g bower  
  
RUN pip3 install --upgrade setuptools pip  
  
RUN git clone https://github.com/jupyter/notebook  
  
RUN cd notebook \  
&& pip3 install -e .  
  
RUN git clone https://github.com/maveme/rascal-codemirror.git  
  
RUN cp -a rascal-codemirror/.
notebook/notebook/static/components/codemirror/mode/  
  
EXPOSE 8888  
RUN jupyter kernelspec install rascal  
  
RUN mkdir home  
  
WORKDIR /home  
  
CMD ["jupyter", "notebook", "--ip","0.0.0.0", "--allow-root"]  

