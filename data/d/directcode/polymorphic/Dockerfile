FROM google/dart:1.8.3  
MAINTAINER Kenneth Endfinger <kaendfinger@gmail.com>  
  
WORKDIR /app  
  
ENV PATH $PATH:$HOME/.pub-cache/bin  
RUN pub global activate -sgit
git://github.com/PolymorphicBot/PolymorphicBot.git  
  
CMD []  
ENTRYPOINT ["polymorphic", "start"]  

