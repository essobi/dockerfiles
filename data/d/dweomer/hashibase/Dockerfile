ARG GPG_IMAGE=dweomer/gnupg  
  
FROM $GPG_IMAGE  
  
ARG HASHICORP_FINGERPRINT=91a6e7f85d05c65630bef18951852d87348ffc4c  
  
ADD
https://keybase.io/hashicorp/pgp_keys.asc?fingerprint=${HASHICORP_FINGERPRINT}
/gpg/import/hashicorp.asc  
  
RUN gpg --import /gpg/import/hashicorp.asc  

