FROM alpine:latest  
  
# Install system dependencies  
RUN ["apk", "update"]  
RUN ["apk", "add", "ruby", "ruby-bundler", "ruby-dev", "ruby-json", "libffi-
dev", "musl-dev", "gcc", "make"]  
  
# Set up user and working space  
RUN ["adduser", "-h", "/nrql_exporter", "-D", "nrql_exporter"]  
USER "nrql_exporter"  
COPY [".", "/nrql_exporter/"]  
WORKDIR "/nrql_exporter"  
# Get ruby dependencies  
RUN ["sh", "-c", "echo 'gem: --no-document' > /nrql_exporter/.gemrc"]  
RUN ["mkdir", ".gems"]  
ENV GEM_HOME="/nrql_exporter/.gems"  
RUN ["bundle", "install"]  
  
# Remove system build tools now they're no-longer needed  
USER "root"  
RUN ["apk", "del", "ruby-bundler", "ruby-dev", "libffi-dev", "musl-dev",
"gcc", "make"]  
  
# Showtime!  
USER "nrql_exporter"  
ENV NRQL_EXPORTER_CONFIG="/nrql_exporter/nrql_exporter.conf"  
CMD ["/nrql_exporter/nrql_exporter"]  

