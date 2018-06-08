FROM openjdk:7  
  
# Install bower  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash \- && apt-get update
&& apt-get install -y nodejs  
RUN npm i -g bower  
  
# Install pip  
RUN wget "https://bootstrap.pypa.io/get-pip.py" && python get-pip.py && rm
get-pip.py  
# Install boto3  
RUN pip install boto3  
  
# Add Grails 2.3.7  
RUN mkdir -p ~/.grails/wrapper/2.3.7 && wget
"http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-2.3.7.zip"
&& unzip grails-2.3.7.zip -d ~/.grails/wrapper/2.3.7 && rm grails-2.3.7.zip  

