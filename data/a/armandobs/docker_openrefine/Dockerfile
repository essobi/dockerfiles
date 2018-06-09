FROM java:8-jdk  
  
MAINTAINER Armando Barbosa <armandobs14@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV PATH $PATH:$JAVA_HOME/bin  
  
#Installing dependencies  
RUN apt-get update && \  
apt-get install -y wget zip ant curl unzip zip inotify-tools && \  
rm -rf /var/lib/apt/lists/*  
  
#Downloading and building Open Refine  
RUN wget -O - --no-check-certificate
https://github.com/OpenRefine/OpenRefine/archive/master.tar.gz | tar -xz  
RUN mv OpenRefine-master OpenRefine; cd ./OpenRefine ; ant clean build;  
  
#Installing RDF Plugin  
RUN cd ./OpenRefine/extensions; \  
wget -O rdf-extension.tar.gz https://github.com/SpazioDati/grefine-rdf-
extension/tarball/export-stream; \  
tar -xzf rdf-extension.tar.gz && rm rdf-extension.tar.gz; \  
mv SpazioDati-grefine-rdf-extension-* rdf-extension; \  
cd ./rdf-extension; \  
JAVA_TOOL_OPTIONS='-Dfile.encoding=UTF-8' ant build  
  
#setting ldpath  
#RUN echo "LD_LIBRARY_PATH=/usr/lib" >> ~/.bashrc && echo "export
LD_LIBRARY_PATH" >> ~/.bashrc  
#Adding entrypoint  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 3333  
CMD ["/start.sh"]

