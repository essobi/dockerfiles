FROM debian:jessie  
  
ENV API_UMBRELLA_VERSION 0.14.4-1~jessie  
  
# Install API Umbrella  
RUN apt-get update && apt-get install -y --no-install-recommends curl
libyaml-0-2 logrotate libxml2 \  
tcl psmisc perl default-jre-headless openjdk-7-jre-headless ca-certificates-
java \  
&& curl -L https://github.com/martel-innovate/api-
umbrella/releases/download/v0.14.4-fiware/api-
umbrella_0.14.4-1.jessie_amd64.deb -o api-umbrella_0.14.4-1.jessie_amd64.deb \  
&& dpkg -i api-umbrella_0.14.4-1.jessie_amd64.deb \  
&& rm -rf /var/cache/apt/archives \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y \  
&& chmod 775 -R /opt/api-umbrella \  
&& chmod 775 -R /etc/api-umbrella \  
&& rm -rf api-umbrella_0.14.4-1.jessie_amd64.deb  
  
# Define mountable directories  
VOLUME ["/etc/api-umbrella", "/opt/api-umbrella/var/db", "/opt/api-
umbrella/var/log"]  
  
# Expose HTTP and HTTPS ports  
EXPOSE 80 443  
# Run the API Umbrella service  
CMD ["api-umbrella", "run"]  

