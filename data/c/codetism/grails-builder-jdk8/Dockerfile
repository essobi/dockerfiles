FROM openjdk:8  
# Install bower  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs  
RUN npm i -g bower  
  
# Install pip  
RUN wget "https://bootstrap.pypa.io/get-pip.py" && python get-pip.py && rm
get-pip.py  
# Install boto3  
RUN pip install boto3  
  
# Add Grails 2.4.4  
RUN mkdir -p ~/.grails/wrapper/2.4.4 && wget
"http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-2.4.4.zip"
&& unzip grails-2.4.4.zip -d ~/.grails/wrapper/2.4.4 && rm grails-2.4.4.zip  
# Add Grails 2.5.1  
RUN mkdir -p ~/.grails/wrapper/2.5.1 && wget
"http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-2.5.1.zip"
&& unzip grails-2.5.1.zip -d ~/.grails/wrapper/2.5.1 && rm grails-2.5.1.zip  
  
# Add Gradle 2.9  
RUN mkdir -p ~/.gradle/wrapper/dists/gradle-2.9-all/1aw2ic01pldw5fkvoq6t1fsz4
&& wget "https://services.gradle.org/distributions/gradle-2.9-all.zip" &&
unzip gradle-2.9-all.zip -d
~/.gradle/wrapper/dists/gradle-2.9-all/1aw2ic01pldw5fkvoq6t1fsz4 && mv
gradle-2.9-all.zip
~/.gradle/wrapper/dists/gradle-2.9-all/1aw2ic01pldw5fkvoq6t1fsz4/ && touch
~/.gradle/wrapper/dists/gradle-2.9-all/1aw2ic01pldw5fkvoq6t1fsz4/gradle-2.9-all.zip.lck
&& touch
~/.gradle/wrapper/dists/gradle-2.9-all/1aw2ic01pldw5fkvoq6t1fsz4/gradle-2.9-all.zip.ok  

