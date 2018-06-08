FROM ring0club/git:2.17.1-r0  
RUN apk add openssh-server --no-cache  
#RUN ssh-keygen -A (generate your own server keys in /etc/ssh volume)  
RUN adduser -D -g 'git' -s /usr/bin/git-shell git && \  
sed --in-place "s/git:!/git:*/" /etc/shadow  
COPY git-shell-commands /home/git/git-shell-commands/  
#VOLUME /home/git /etc/ssh  
ENTRYPOINT ["/usr/sbin/sshd", "-D", "-e"]  

