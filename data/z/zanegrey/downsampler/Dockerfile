# Specifies the starting image from which this docker image will be built  
FROM debian  
  
# Necessary to get the latest packages  
RUN apt-get update -y  
  
# Notice the -y switch to ensure that any prompts are bypassed  
RUN apt-get install -y openjdk-7-jdk  
  
# Ensure that we are using the correct java version  
RUN update-alternatives --set java /usr/lib/jvm/java-7-openjdk-
amd64/jre/bin/java  
  
RUN apt-get install -y maven git  
  
RUN cd /root && git clone \--recursive https://github.com/docker-for-the-
enterprise-demo/blog-demo.git  
  
# The workdir resets after each intermediate RUN (each RUN is processed in its  
# own image) so group cd and commands together  
RUN cd /root/blog-demo && git checkout blog1-initial  
  
RUN cd /root/blog-demo/simple-spring-app/app && mvn package  
  
RUN mkdir -p /var/opt/downsample/download  
  
RUN mkdir -p /var/opt/downsample/static  
  
# CMD is not run as part of the image, but rather is the default command that  
# will be executed when a container is executed.  
CMD java -jar /root/blog-demo/simple-spring-app/app/target/simple-app.jar  
  

