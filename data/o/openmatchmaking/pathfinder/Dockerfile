# Stage 1: Build an application from a source code  
FROM rust:1.23 as build  
  
# Get the latest code from pathfinder's master branch  
RUN apt-get update && apt-get install git  
RUN git clone https://github.com/OpenMatchmaking/pathfinder.git  
  
# And built it in release mode  
WORKDIR pathfinder/pathfinder  
RUN cargo build --release  
  
# ------------------------------------------------------------  
# Stage 2: Create a separate image for the compiled application  
FROM debian:stretch-slim  
RUN apt-get update && apt-get -y install openssl  
  
# Copies the binary from the "build" stage to the current stage  
WORKDIR /app  
COPY \--from=build pathfinder/pathfinder/target/release/pathfinder /app  
  
ENV SECURED_MODE="no" \  
VALIDATE_TOKEN="no" \  
CONFIG_PATH="" \  
LISTENED_IP="127.0.0.1" \  
LISTENED_PORT="9000" \  
RABBITMQ_HOST="127.0.0.1" \  
RABBITMQ_PORT="5672" \  
RABBITMQ_VIRTUAL_HOST="vhost" \  
RABBITMQ_USER="user" \  
RABBITMQ_PASSWORD="password" \  
REDIS_HOST="127.0.0.1" \  
REDIS_PORT="6379" \  
REDIS_PASSWORD="" \  
JWT_SECRET="secret" \  
SSL_CERTIFICATE="" \  
SSL_KEY="" \  
LOG_LEVEL="info"  
EXPOSE 9000  
# Configures the startup  
COPY ./run.sh ./run.sh  
CMD ["./run.sh"]  

