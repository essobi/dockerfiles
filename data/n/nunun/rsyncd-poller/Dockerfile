FROM alpine  
RUN apk --update add rsync curl tzdata  
ADD env.sh /  
ADD pre-poll.sh /  
ADD post-poll.sh /  
ADD pre-rsync.sh /  
ADD post-rsync.sh /  
ADD update.sh /  
ADD start.sh /  
CMD sh /start.sh  

