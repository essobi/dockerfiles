FROM node:alpine  
  
RUN apk update && apk add zip curl  
  
# Insall superpowers-core  
RUN curl -L $( \  
curl -s https://api.github.com/repos/superpowers/superpowers-
core/releases/latest \  
| grep browser_download_url \  
| cut -d '"' -f 4\  
) -o /tmp/superpowers-core.zip && \  
mkdir /superpowers-core && \  
unzip -o /tmp/superpowers-core.zip -d /superpowers-core && \  
mv /superpowers-core/superpowers-core-v*/* /superpowers-core/ && \  
rm -r /tmp/superpowers-core.zip /superpowers-core/superpowers-core-v*  
  
WORKDIR /superpowers-core  
  
# Install the game system  
RUN node server install game  
  
ADD start.sh .  
  
# Add password to the config file  
RUN printf '{\n"password":"unsecure"\n}' > config.json  
  
EXPOSE 4237 4238  
ENTRYPOINT ["sh", "start.sh"]

