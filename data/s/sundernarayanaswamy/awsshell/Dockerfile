FROM alpine  
  
RUN apk --no-cache update && \  
apk --no-cache add python3 groff less && \  
pip3 --no-cache-dir install awscli aws-shell && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /home  
  
CMD bash -c "aws-shell"  
  
# alias aws='docker run -it --rm \  
# -v $HOME:/root -v $PWD:/home \  
# sundernarayanaswamy/awsshell'  

