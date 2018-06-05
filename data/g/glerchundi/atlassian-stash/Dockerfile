# Image: glerchundi/atlassian-stash:3.0  
FROM glerchundi/base-with-oracle-java7:12.04  
MAINTAINER Gorka Lerchundi Osa <glertxundi@gmail.com>  
  
# Environment  
ENV STASH_HOME /home/stash  
ENV STASH_VERSION 3.0.4  
ENV STASH_URL
http://downloads.atlassian.com/software/stash/downloads/atlassian-
stash-$STASH_VERSION.tar.gz  
  
# Dependencies  
RUN apt-get install -y git  
  
# Stash  
RUN wget -P /opt $STASH_URL  
RUN tar xvzf /opt/atlassian-stash-$STASH_VERSION.tar.gz -C /opt  
RUN rm /opt/atlassian-stash-$STASH_VERSION.tar.gz  
RUN ln -s /opt/atlassian-stash-$STASH_VERSION /opt/atlassian-stash  
  
ADD assets/ /app/  
RUN chmod 755 /app/init /app/setup/install  
RUN /app/setup/install  
  
VOLUME ["/home/stash"]  
  
EXPOSE 7990  
ENTRYPOINT ["/app/init"]  
CMD ["app:start"]  

