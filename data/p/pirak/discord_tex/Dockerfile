FROM debian:jessie  
MAINTAINER Benedikt Fein "benedikt.fein@gmail.com"  
RUN apt-get update -yqq \  
&& apt-get install --no-install-recommends -y openssl libssl-dev libsodium-dev
libsodium13 unzip curl imagemagick  
  
RUN apt-get install -y texlive-full \  
&& apt-get --purge remove -y .\\*-doc$ \  
&& apt-get clean -y  
  
WORKDIR /bot  
  
RUN mkdir -p /bot && cd /bot && curl -L
"https://gitlab.com/pirak/discord_tex/builds/artifacts/master/download?job=build"
> artifacts.zip \  
&& unzip artifacts.zip && cp target/release/discord_tex . \  
&& chmod +x discord_tex  
  
ENV PATH $PATH:/bot  
ENV NAME DISCORD_TOKEN  
  
ENTRYPOINT ["discord_tex"]  

