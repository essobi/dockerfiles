FROM java:openjdk-8u40  
MAINTAINER Hideki IGARASHI <hideki.develop@gmail.com>  
  
ENV GITBUCKET_VERSION 2.8  
RUN useradd --home-dir /opt/gitbucket --create-home --system --shell /bin/sh
gitbucket  
RUN mkdir /var/lib/gitbucket  
RUN chown gitbucket:gitbucket /var/lib/gitbucket  
  
RUN curl -L -o /opt/gitbucket/gitbucket.war
https://github.com/takezoe/gitbucket/releases/download/$GITBUCKET_VERSION/gitbucket.war  
  
COPY entry-point.sh /  
RUN chmod +x /entry-point.sh  
  
USER gitbucket  
  
VOLUME ["/var/lib/gitbucket"]  
  
EXPOSE 8080 29418  
ENTRYPOINT ["/entry-point.sh"]  

