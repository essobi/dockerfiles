# Install all the cheminformatic packages  
FROM mdstudio/mdstudio_docker_conda:0.0.1  
RUN apt-get update -y && apt-get install wget libopenbabel-dev openbabel -y  
  
COPY . /home/mdstudio/lie_structures  
  
RUN chown mdstudio:mdstudio /home/mdstudio/lie_structures  
  
RUN conda install -c rdkit rdkit && \  
conda install -c openbabel openbabel && \  
conda install -c bioconda java-jdk && \  
conda install -c conda-forge jpype1 && \  
conda install -c speleo3 indigo  
  
RUN pip install pydpi  
  
WORKDIR /home/mdstudio  
  
RUN wget https://github.com/cdk/cdk/releases/download/cdk-2.1.1/cdk-2.1.1.jar  
  
RUN wget https://bitbucket.org/dan2097/opsin/downloads/opsin-1.3.0-jar-with-
dependencies.jar  
  
ENV CLASSPATH=/home/mdstudio/cdk-2.1.1.jar:/home/mdstudio/opsin-1.3.0-jar-
with-dependencies.jar:$CLASSPATH  
  
ENV JPYPE_JVM=/usr/local/jre/lib/amd64/server/libjvm.so  
  
RUN pip install
"https://github.com/cinfony/cinfony/tarball/master#egg=cinfony-1.2"  
  
WORKDIR /home/mdstudio/lie_structures  
  
RUN pip install -e .  
  
CMD ["bash", "entry_point_lie_structures.sh"]  

