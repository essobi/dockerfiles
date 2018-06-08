FROM openjdk:7  
LABEL maintainer "Philippe Poumaroux <poum@cpan.org>"  
  
ENV VERSION=6.5.3  
  
ENTRYPOINT ["/opt/Sencha/Cmd/6.5.3/sencha"]  
  
RUN curl -o /cmd.run.zip http://cdn.sencha.com/cmd/$VERSION/no-
jre/SenchaCmd-$VERSION-linux-amd64.sh.zip && \  
unzip -p /cmd.run.zip > /cmd-install.run && \  
chmod +x /cmd-install.run && \  
/cmd-install.run -q -dir /opt/Sencha/Cmd/$VERSION && \  
install -dm777 -o root -g root /opt/Sencha/Cmd/repo && \  
rm /cmd-install.run /cmd.run.zip && \  
apt-get update && apt-get install -y --no-install-recommends \  
ruby \  
libffi6 \  
build-essential \  
ruby-dev \  
libffi-dev && \  
gem update --system && \  
gem install compass && \  
apt-get remove -y ruby-dev build-essential libffi-dev && \  
rm -rf /var/lib/apt/lists/*  

