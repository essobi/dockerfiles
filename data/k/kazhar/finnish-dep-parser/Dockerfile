#Docker image of Finnish dependency parser developed by Turku NLP group.  
#https://github.com/TurkuNLP/Finnish-dep-parser  
FROM python:2.7-alpine  
  
RUN apk add --update --no-cache bash openjdk8 curl-dev curl wget zip \  
&& apk update \  
&& apk add ca-certificates \  
&& update-ca-certificates  
  
WORKDIR /  
  
#copy scripts to be used in the docker image  
COPY scripts/image/*.* ./  
  
#Install Maven  
RUN ["/bin/bash" ,"install_maven.sh","3.5.2"]  
  
#server4dev is for development use  
#Docker uses layered filesystem and each line of Dockerfile is maintained in
the image  
#TODO: more refactoring for image size http://blog.replicated.com/refactoring-
a-dockerfile-for-image-size/  
#when building docker, mvn dependencies are always downloaded  
#using this server4dev dir and packaging it, mvn downloads dependencies once
and image with dependencies is stored to docker cache  
#and if you change Dockerfile after the following three lines, Docker uses
cached image where dependencies are already downloaded.  
#if adding new dependencies to pom.xml, copy pom.xml from server directory to
server4dev directory before building docker image  
COPY server4dev ./server4dev/  
RUN PATH=/maven/bin:$PATH && cd server4dev && mvn package  
  
#Install Finnish-dep-parser  
#Uses fork: https://github.com/samisalkosuo/Finnish-dep-parser  
#uses specific commit ID as parameter  
RUN ["/bin/bash"
,"install_findepparser.sh","fc8511cd16541e3b07072352d5801b54a5c05cf3"]  
  
WORKDIR /Finnish-dep-parser  
  
#copy scripts to current dir  
RUN mv ../*.py . && mv ../*.sh .  
  
#add server code  
COPY server ./server/  
COPY server/resources ./finwordnet/  
RUN ["/bin/bash" ,"package_parserserver.sh"]  
  
#add modified Finnish dependency parser files  
COPY scripts/depparser/*.* ./  
  
RUN chmod 755 *sh  
  
#add testfiles  
#RUN mkdir testfiles  
#ADD test ./testfiles/  
#Port 9876 is hardcoded servlet server port  
EXPOSE 9876  
CMD ["/bin/bash", "start_parser_server.sh"]  
  
#execute server within image:  
#java -Xmx2g -jar fin-dep-parser-server-jar-with-dependencies.jar  
#CMD ["/bin/bash"]  

