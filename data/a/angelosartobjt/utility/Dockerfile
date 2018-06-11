FROM openjdk:8  
# includes curl, java, git  
RUN apt-get update  
  
# install zsh  
RUN apt-get install -y zsh  
  
CMD ["zsh"]  
  
# install oh-my-zsh  
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" || true  
COPY .zshrc /root  
  
# install liquibase  
RUN curl -LOJ
https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-3.5.3/liquibase-3.5.3-bin.tar.gz  
RUN mkdir /opt/liquibase  
RUN tar -xzf liquibase-3.5.3-bin.tar.gz -C /opt/liquibase  
RUN chmod +x /opt/liquibase/liquibase  
RUN ln -s /opt/liquibase/liquibase /usr/local/bin  
RUN rm -f liquibase-3.5.3-bin.tar.gz  
  
# install man and vim  
RUN apt-get install -y man vim  

