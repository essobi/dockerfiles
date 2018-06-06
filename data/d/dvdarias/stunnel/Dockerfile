FROM alpine:latest  
  
RUN apk add --update openssh  
  
RUN mkdir /stunnel  
WORKDIR /stunnel  
  
#Copy the auth command that gets the authorized keys  
RUN mkdir auth-commands  
RUN printf '#!/bin/sh'\\\n'cat /stunnel/authorized_keys' > auth-
commands/auth.sh  
RUN chmod 700 auth-commands auth-commands/auth.sh /stunnel  
  
#Copy the executables  
COPY server server  
COPY client client  
  
#Generate the develop auth keys  
RUN mkdir develop-id  
RUN ssh-keygen -q -P "" -C test@develop -f develop-id/id_rsa  
#Build the command that automatically echoes the public key for the server on
develop mode  
RUN cat develop-id/id_rsa.pub > auth-commands/auto-auth.sh  
RUN sed -i -e 's/^/#!\/bin\/sh\necho \"/' -e 's/$/\"/' auth-commands/auto-
auth.sh  
RUN chmod 700 auth-commands/auto-auth.sh  
  

