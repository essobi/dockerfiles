FROM rust  
  
EXPOSE 80  
# Install build tools  
RUN rustup default nightly  
  
# Copy app and set working directory  
COPY . /app  
WORKDIR /app  
  
# Compile  
RUN cargo build --release  
  
# Setup environnement and run  
ENV ROCKET_ADDRESS="0.0.0.0"  
ENV ROCKET_PORT=80  
CMD ["cargo", "run", "--release"]  

