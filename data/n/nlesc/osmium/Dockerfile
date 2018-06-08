FROM debian:jessie  
MAINTAINER Joris Borgdorff <j.borgdorff@esciencecenter.nl>  
  
# Remove warnings during apt-get  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Create directories  
RUN mkdir -p /usr/local/src /var/lib/osmium/.ssh /var/lib/osmium/sandbox  
# Install runtime dependencies (Debian Jessie is needed for gradle)  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
openjdk-7-jre-headless \  
openssh-client \  
openjdk-7-jdk \  
gradle \  
git \  
ant  
  
RUN git clone https://github.com/NLeSC/xenon /usr/local/src/xenon \  
&& cd /usr/local/src/xenon \  
&& git checkout develop \  
&& ant  
  
RUN git clone https://github.com/NLeSC/osmium.git /usr/local/src/osmium \  
&& cd /usr/local/src/osmium \  
&& git checkout 0bca57af241c2c2cc5f2880f7b8afc44c97c21d7 \  
&& cp /usr/local/src/xenon/lib/*.jar lib \  
&& cp /usr/local/src/xenon/lib/*/*.jar lib \  
&& cp /usr/local/src/xenon/dist/nlesc-xenon-*/lib/xenon-*.jar lib/xenon.jar \  
&& gradle fatJar \  
&& cp build/libs/osmium-*-all.jar /var/lib/osmium/osmium.jar \  
&& cp joblauncher.yml-dist /var/lib/osmium/joblauncher.yml  
# Set permissions  
RUN groupadd -r osmium \  
&& useradd -d /var/lib/osmium -g osmium osmium \  
&& chown -R osmium:osmium /var/lib/osmium  
  
USER osmium  
WORKDIR /var/lib/osmium  
CMD ["/usr/bin/java", "-jar", "osmium.jar", "server", "joblauncher.yml"]  

