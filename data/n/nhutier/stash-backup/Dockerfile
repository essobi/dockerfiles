FROM java:7  
RUN wget https://maven.atlassian.com/content/repositories/atlassian-
public/com/atlassian/stash/backup/stash-backup-distribution/1.7.0/stash-
backup-distribution-1.7.0.zip  
RUN unzip stash-backup-distribution-1.7.0.zip -d /  
RUN mkdir /var/stashbackup  
RUN mkdir /var/stashwork  
VOLUME /var/stashbackup  
WORKDIR /var/stashbackup  
ENV STASH_HOME=/var/stashwork  

