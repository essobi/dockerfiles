FROM alpine  
MAINTAINER paco falder <francisco-esteban.falder-rodriguez@capgemini.com>  
RUN apk update  
RUN apk add bash  
RUN apk add openjdk8  
RUN apk add apache-ant --update-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \  
\--allow-untrusted  
#Drop salesforce migration tool into the ant/lib so it can be used for
deployment  
COPY salesforce_ant/ant-salesforce.jar /usr/share/java/apache-ant/lib/  
ENV ANT_HOME /usr/share/java/apache-ant  
ENV PATH $PATH:$ANT_HOME/bin

