FROM openjdk:8-jre-alpine  
  
RUN apk add --no-cache bash gawk sed grep bc coreutils  
  
ARG SHELL_VERSION=1.0.0  
ADD
https://oss.sonatype.org/service/local/repositories/releases/content/website/automate/shell/$SHELL_VERSION/shell-$SHELL_VERSION.jar
/bin/aws  
  
RUN chmod +x /bin/aws  
  
CMD ["/bin/aws"]  

