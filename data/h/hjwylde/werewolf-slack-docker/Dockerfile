FROM haskell:7.10.3  
RUN stack --resolver lts-6.2 install werewolf-slack-1.0.2.0 werewolf  
RUN stack --resolver lts-6.2 install werewolf-1.5.1.1  
ENTRYPOINT ["werewolf-slack"]  
  
EXPOSE 80  

