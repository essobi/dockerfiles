FROM bucharestgold/centos7-s2i-nodejs:7.x  
  
ENV ANGULAR_CLI_VERSION latest  
  
USER root  
  
# prepare a user which runs everything locally! - required in child images!  
RUN useradd --user-group --create-home --shell /bin/false app  
RUN npm install -g @angular/cli@$ANGULAR_CLI_VERSION >/dev/null 2>&1 && npm
cache clean  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/ $STI_SCRIPTS_PATH  
  
USER 1001

