FROM continuumio/miniconda3  
  
RUN apt-get update && apt-get install -y gcc openjdk-8-jdk && rm -rf
/var/lib/apt/lists/*  
RUN conda install cython boto3 scikit-image  
RUN pip install -q pyjnius  
RUN curl -o /opt/loci_tools.jar http://downloads.openmicroscopy.org/bio-
formats/5.8.2/artifacts/loci_tools.jar  
  
COPY bfextractor.py /opt  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV CLASSPATH /opt/loci_tools.jar  
WORKDIR /tmp/aws  
  
ENTRYPOINT ["python", "/opt/bfextractor.py"]  

