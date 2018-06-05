# Build only image  
FROM ekidd/rust-musl-builder as builder  
  
WORKDIR /app  
RUN sudo chown -R rust:rust .  
# Update the registry. This is repeated with the build step but the buld of
the work can be cached here.  
# However, over time this cache will diverge from the current state of the
registry and may need to be re-run  
RUN cargo search  
  
# Cache bust here, if it's cachable put it above this line  
ADD . .  
RUN cargo build --release  
  
## App image  
FROM scratch  
  
COPY \--from=builder /app/target/x86_64-unknown-linux-musl/release/kubesm
/kubesm  
  
CMD ["/kubesm"]  

