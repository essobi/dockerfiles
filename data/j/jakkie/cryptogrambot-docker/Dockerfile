FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y unzip wget curl apt-transport-https
&& apt-get clean  
  
ARG CRYPTOGRAMBOT_VERSION=0.3.311  
ENV CRYPTOGRAMBOT_VERSION ${CRYPTOGRAMBOT_VERSION}  
  
RUN mkdir -p /cryptogrambot  
WORKDIR /cryptogrambot  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-get update  
RUN apt-get install -y dotnet-sdk-2.0.2  
  
RUN wget
https://github.com/mehtadone/CryptoGramBot/releases/download/CryptoGramBot-v$CRYPTOGRAMBOT_VERSION/CryptoGramBot-v$CRYPTOGRAMBOT_VERSION.zip  
RUN unzip CryptoGramBot-v$CRYPTOGRAMBOT_VERSION.zip  
  
VOLUME /cryptogrambot/  
  
CMD dotnet CryptoGramBot.dll  
  
EXPOSE 5002  

