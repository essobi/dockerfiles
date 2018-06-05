FROM ingensi/play-framework  
  
COPY . /data  
  
WORKDIR /data  
  
RUN yum install -y tar openssl mvn  
  
RUN mvn clean test site  
  
RUN buildDate=`date +"%m-%d-%y-%H:%M:%S"` && \  
cp -r target/site/allure-maven-plugin /tmp/$buildDate &&\  
git checkout gh-pages && git pull && \  
mv /tmp/$buildDate builds/$buildDate && \  
git add -A && git commit -m "CI build form $buildDate" && git push  
  
RUN activator universal:package-xz-tarball  
  
RUN rm -rf *  

