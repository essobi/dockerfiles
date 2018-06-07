  
#  
# Bootstrap Invoice Builder Dockerfile  
#  
FROM ubuntu:trusty  
  
MAINTAINER Steven Matison "steven.matison@gmail.com"  
WORKDIR /home/invoice  
  
COPY . /home/invoice  
  
# setup the app locally  
RUN mkdir /home/invoice/logos && chmod 777 /home/invoice/logos  
RUN mkdir /home/invoice/pdfs && chmod 777 /home/invoice/pdfs  
RUN cp /home/invoice/logo.png /home/invoice/logos  
  
# Update the server and install dependencies  
RUN apt-get update && apt-get install -y nano wget dialog net-tools nginx
php5-fpm php5-mysql  
  
# update nginx server  
RUN rm -rf /etc/nginx/sites-enabled/default && cp /home/invoice/invoice.conf
/etc/nginx/sites-available && ln -s /etc/nginx/sites-available/invoice.conf
/etc/nginx/sites-enabled/invoice  
  
# get db.credentials  
RUN wget --output-document=db.credentials
http://sceneserver.com/api/auth/?app=BootstrapInvoiceBuilder  
  
#set 750 perms on private files  
RUN chmod 750 /home/invoice/db.credentials && chmod 750
/home/invoice/invoice_view.php && chmod 750
/home/invoice/api/file_upload_parser.php && chmod 750
/home/invoice/phpMailer.php && chmod 750 /home/invoice/phpToPDF.php  
  
# Expose ports  
EXPOSE 80  
# Set the default command to execute  
CMD /bin/sh -c php5-fpm -d variables_order="EGPCS" && (tail -F
/var/log/nginx/error.log &) && exec nginx -g "daemon off;"  

