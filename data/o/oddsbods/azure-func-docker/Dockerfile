FROM microsoft/dotnet:2.0-runtime  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install curl gnupg gnupg2 apt-transport-https -y  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-artful-prod artful main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-get update  
RUN apt-get install azure-functions-core-tools -y  
  
RUN apt-get install nginx -y  
COPY ./etc/nginx/sites-available/default /etc/nginx/sites-available/  
COPY ./var/www/html/** /var/www/html/  
  
COPY README.md /var/www/html/  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]

