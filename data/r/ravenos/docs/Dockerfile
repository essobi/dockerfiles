FROM rust  
  
EXPOSE 80  
# Install build tools  
RUN rustup default nightly  
RUN apt-get update && apt-get install -y \  
doxygen \  
graphviz  
  
# Copy app and set working directory  
COPY . /app  
WORKDIR /app  
  
# Compile  
RUN cargo update  
RUN cargo build --release  
  
# Built docs will go there  
VOLUME /docs  
  
# Setup environnement and run  
#  
# You may want to edit these values  
ENV ROCKET_ADDRESS="0.0.0.0"  
ENV ROCKET_PORT=80  
ENV RAVEN_DOCS_TOKEN=""  
ENV RAVEN_DOCS_PATH="/docs"  
CMD ["cargo", "run", "--release"]  

