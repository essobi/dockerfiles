FROM therecipe/qt:linux  
  
#RUN mkdir ~/.ssh/ && echo -e "Host github.com\n\tStrictHostKeyChecking no\n"
> ~/.ssh/config  
RUN mkdir -p ~/.ssh/ && touch ~/.ssh/known_hosts  
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

