FROM java:7  
  
ENV VERSION 1.0.3  
  
ENV KOTLIN_COMPILER_URL
https://github.com/JetBrains/kotlin/releases/download/v${VERSION}/kotlin-
compiler-${VERSION}.zip  
  
#RUN apt-get udpate &&  
# apt-get install -y &&  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/*  
  
RUN wget $KOTLIN_COMPILER_URL -O /tmp/a.zip && \  
unzip /tmp/a.zip -d /opt && \  
rm /tmp/a.zip  
  
ENV PATH $PATH:/opt/kotlinc/bin  

