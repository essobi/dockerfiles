FROM alpine  
RUN apk add --no-cache gnupg  
CMD /usr/bin/gpg --passphrase `echo -n $PASSPHRASE | base64 -d` --batch --no-
tty --yes --output $ENC \--symmetric --cipher-algo AES256 $RAW  

