FROM java:8  
MAINTAINER Baptiste Mathus <batmat@batmat.net>  
  
RUN wget http://apache.mindstudios.com/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.zip && \  
unzip apache-maven-3.3.9-bin.zip && \  
rm apache-maven-3.3.9-bin.zip  
ENV PATH /apache-maven-3.3.9/bin:$PATH  
  
RUN apt-get install -y \  
git && \  
apt-get clean  
  
# Cloning + "warming" up the maven local cache/repository for 1.x and 2.x  
RUN git clone https://github.com/jenkinsci/jenkins &&\  
cd jenkins && \  
mvn clean package -DskipTests dependency:go-offline && \  
git checkout 2.0 && \  
mvn clean package -DskipTests dependency:go-offline && \  
mvn clean  
  
WORKDIR jenkins  
  
ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-
static -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha1sum -c -  
  
ADD checkout-and-start.sh /checkout-and-start.sh  
RUN chmod +x /checkout-and-start.sh  
  
EXPOSE 8080  
ENTRYPOINT ["/bin/tini", "--", "/checkout-and-start.sh"]  

