FROM ubuntu  
ENV TEST_ENV true  
ADD test_file /  
RUN apt-get update  
RUN apt-get install -y fortune cowsay  
CMD /usr/games/fortune | /usr/games/cowsay -f $(ls /usr/share/cowsay/cows/ |
shuf -n1)  

