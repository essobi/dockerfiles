# Dockerfile for building GitPitch images  
# Set the base image of ubuntu with scala and sbt installed  
FROM hseeberger/scala-sbt  
  
# File author / maintainer  
MAINTAINER lexsys  
  
# Build GitPitch binary  
RUN git clone https://github.com/gitpitch/gitpitch.git && \  
cd gitpitch && \  
sbt dist && \  
mv target/universal/server-2.0.zip /srv/ && \  
cd /srv && \  
unzip -q server-2.0.zip && \  
mv server-2.0 gitpitch  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
apt-get update && apt-get install -y \  
nodejs \  
&& rm -rf /var/lib/apt/lists/*  
# Install node libraries for PDF export  
RUN cd /srv/gitpitch && \  
npm install --no-package-lock decktape phantomjs-prebuilt && \  
npm cache --force clean && \  
cd /srv/gitpitch/node_modules && \  
mkdir decktape/bin && \  
mkdir decktape/lib && \  
cp phantomjs-prebuilt/bin/phantomjs decktape/bin/ && \  
cp -R phantomjs-prebuilt/lib/* decktape/lib  
# Running phase  
FROM openjdk:8u151-jre-slim  
  
# Add environment variables substitution  
RUN apt-get update && apt-get install -y \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
COPY --from=0 /srv/gitpitch /srv/gitpitch  
COPY bin/start.sh .  
COPY conf/application.conf.template .  
  
# Listens on port 9000  
EXPOSE 9000  
# Start scrip  
ENTRYPOINT ["./start.sh"]  

