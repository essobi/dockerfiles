FROM cagiti/docker-alpine-ide-base:latest  
MAINTAINER Cai Cooper "caicooper82@gmail.com"  
ENV IDEA_CONFIG_PREFIX IdeaIC  
ENV IDEA_PRODUCT ideaIC  
ENV IDEA_MAJOR 2017  
ENV IDEA_MINOR 1  
ENV IDEA_FLAVOUR 3  
RUN curl -L
http://download.jetbrains.com/idea/ideaIC-${IDEA_MAJOR}.${IDEA_MINOR}.${IDEA_FLAVOUR}-no-
jdk.tar.gz | tar zx -C /opt && \  
mv /opt/idea* /opt/intellij  
  
USER developer  
CMD ["/opt/intellij/bin/idea.sh"]  

