FROM alpine  
MAINTAINER Ben Edwards <ben@cloudinit.nz>  
RUN apk update  
RUN apk add bash  
RUN apk add openjdk8  
RUN apk add apache-ant --update-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \  
\--allow-untrusted  
RUN apk add git  
# Drop salesforce migration tool into the ant/lib so it can be used for
deployment  
COPY ant-salesforce.jar /usr/share/java/apache-ant/lib/  
ENV ANT_HOME /usr/share/java/apache-ant  
ENV PATH $PATH:$ANT_HOME/bin

