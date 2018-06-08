FROM mailhog/mailhog:latest  
MAINTAINER Alexander Eimer <https://github.com/aeimer>  
# Published from http://github.com/aeimer  
ENV MH_USER mhog  
ENV MH_PWD mhog123  
  
ENTRYPOINT echo $MH_USER:$(MailHog bcrypt $MH_PWD) > auth_file && MailHog
-auth-file=auth_file  

