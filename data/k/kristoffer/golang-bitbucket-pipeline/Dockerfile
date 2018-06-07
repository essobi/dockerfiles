FROM golang:1.9  
RUN git config --global url."git@bitbucket.org:".insteadOf
"https://bitbucket.org/"  
RUN mkdir -p ~/.ssh && ssh-keyscan -H bitbucket.org >> ~/.ssh/known_hosts  
RUN curl https://glide.sh/get | sh  

