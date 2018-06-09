FROM openjdk:8-alpine  
LABEL maintainer "Alexander Groß <agross@therightstuff.de>"  
  
EXPOSE 8111  
WORKDIR /teamcity  
  
RUN echo Creating teamcity user and group with static ID of 3000 && \  
addgroup -g 3000 -S teamcity && \  
adduser -g "JetBrains TeamCity" -S -h "$(pwd)" -u 3000 -G teamcity teamcity  
  
RUN echo Installing packages && \  
apk add --no-cache bash \  
coreutils \  
ca-certificates \  
git \  
libressl \  
tomcat-native \  
wget  
  
RUN TEAMCITY_VERSION=57985 && \  
\  
DOWNLOAD_URL=https://download.jetbrains.com/teamcity/eap/TeamCity-$TEAMCITY_VERSION.tar.gz
&& \  
echo Downloading $DOWNLOAD_URL to $(pwd) && \  
wget "$DOWNLOAD_URL" \--progress bar:force:noscroll --output-document
teamcity.tar.gz && \  
\  
echo Extracting to $(pwd) && \  
tar -xzvf teamcity.tar.gz --directory . && \  
rm -f teamcity.tar.gz && \  
mv TeamCity/* . && \  
rm -rf TeamCity && \  
\  
chown -R teamcity:teamcity .  
  
# Allow TeamCity to retrieve the client IP and host header when running behind
a proxy.  
#
https://confluence.jetbrains.com/display/TCD9/How+To...#HowTo...-Tomcatsettings  
RUN sed --in-place --expression 's_</Host>.*$_\  
<Valve className="org.apache.catalina.valves.RemoteIpValve"\n\  
protocolHeader="x-forwarded-proto"\n\  
remoteIpHeader="x-forwarded-for" />\n\  
&_' conf/server.xml  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["teamcity-server", "run"]  
  
USER teamcity  

