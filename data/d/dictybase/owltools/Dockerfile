FROM maven:3.5.0-jdk-8-alpine  
MAINTAINER 'Siddhartha Basu<sidd.basu@gmail.com>'  
ARG user=cybersiddhu  
ARG tag=v0.3.0  
# Add required softare for intermine  
RUN apk add --no-cache curl git perl bash make \  
&& addgroup -g 1000 -S $user && adduser -G $user -D -u 1000 -S $user  
USER $user  
WORKDIR /home/$user  
RUN git clone \--branch $tag https://github.com/owlcollab/owltools.git
owltools \  
&& cd /home/$user/owltools/OWLTools-Parent \  
&& mvn clean install -DskipTests  
RUN chmod u+x /home/$user/owltools/OWLTools-Runner/bin/owltools  
ENV PATH $PATH:/home/$user/owltools/OWLTools-
Runner/bin:/home/$user/owltools/OWLTools-Oort/bin  
ENV MAVEN_CONFIG=/home/$user/.m2  

