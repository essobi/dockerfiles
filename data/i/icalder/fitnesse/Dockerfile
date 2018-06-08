FROM openjdk:8-jre  
  
ENV FITNESSE_RELEASE 20161106  
ENV FITSHARP_RELEASE 2.5  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
echo "deb http://download.mono-project.com/repo/debian wheezy-libjpeg62-compat
main" | tee -a /etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update && apt-get install -y \  
mono-complete && \  
useradd -u 1000 -s /bin/false -r fitnesse && \  
mkdir /opt/fitnesse && \  
chown fitnesse /opt/fitnesse && \  
mkdir /opt/fitsharp && \  
curl -fsSL -o /usr/local/lib/fitnesse-standalone.jar
"http://www.fitnesse.org/fitnesse-
standalone.jar?responder=releaseDownload&release=$FITNESSE_RELEASE" && \  
curl -fsSL -o "/opt/fitsharp/release$FITSHARP_RELEASE.zip"
"https://github.com/jediwhale/fitsharp/releases/download/$FITSHARP_RELEASE/release.$FITSHARP_RELEASE.net.40.zip"
&& \  
unzip -d /opt/fitsharp "/opt/fitsharp/release$FITSHARP_RELEASE.zip" && \  
rm -f "/opt/fitsharp/release$FITSHARP_RELEASE.zip" && \  
echo '#!/usr/bin/env bash' > /opt/fitsharp/runner.sh && \  
echo '/usr/bin/mono /opt/fitsharp/Runner.exe $@' >> /opt/fitsharp/runner.sh &&
\  
echo '#!/usr/bin/env bash' > /opt/fitsharp/runnerw.sh && \  
echo '/usr/bin/mono /opt/fitsharp/RunnerW.exe $@' >> /opt/fitsharp/runnerw.sh
&& \  
chmod +x /opt/fitsharp/*.exe /opt/fitsharp/*.sh  
  
WORKDIR /opt/fitnesse  
VOLUME /opt/fitnesse  
USER fitnesse  
ENTRYPOINT ["java", "-Xmx256m", "-jar", "/usr/local/lib/fitnesse-
standalone.jar", "-p", "8080"]  
EXPOSE 8080

