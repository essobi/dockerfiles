FROM openjdk:8-alpine  
  
ENV PLAY_VERSION "1.4.4"  
ENV PLAY_HOME /opt/play/play-${PLAY_VERSION}  
  
LABEL maintainer.name="Anthony PERIQUET"  
LABEL maintainer.email="anthony@periquet.net"  
LABEL version=${PLAY_VERSION}  
LABEL description="Play Framework v${PLAY_VERSION}"  
  
# Play Framework installation  
RUN apk add --no-cache --quiet curl python && \  
mkdir -p /opt/play && cd /opt/play && \  
# Download play framework  
curl --fail --silent --show-error --location --remote-name
https://downloads.typesafe.com/play/${PLAY_VERSION}/play-${PLAY_VERSION}.zip
&& \  
# Extract and clean archive  
unzip play-${PLAY_VERSION}.zip && rm play-${PLAY_VERSION}.zip && \  
# Set execution  
chmod +x /opt/play/play-${PLAY_VERSION}/play  
# Create application folder  
RUN mkdir -p /app  
  
WORKDIR /app  
  
EXPOSE 9000  
HEALTHCHECK \--interval=30s --timeout=3s \  
CMD curl --fail http://localhost:9000/ || exit 1  
  
# Define entrypoint  
ENTRYPOINT ["/opt/play/play-1.4.4/play"]  
# Define command (entrypoint parameters)  
# - Start application located in /app directory  
# - Install dependencies on start  
# - Force port to 9000  
CMD ["run", "/app", "--deps", "--http.port=9000"]

