FROM java:jre-alpine  
  
RUN apk add --no-cache curl  
COPY . /usr/src/app  
WORKDIR /opt/iota  
CMD ["java", "-XX:+DisableAttachMechanism", "-jar", "/usr/src/app/IRI.jar",
"14265", "udp://188.192.225.109:14265", "udp://94.23.121.27:14265",
"udp://99.238.224.192:14265", "udp://148.251.233.147:14265"]  

