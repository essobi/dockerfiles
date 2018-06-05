FROM dehy/adminer  
# move installed php/css to html-base and nginx start script to run-base  
RUN mv /var/www/html /var/www/html-base && \  
mv /etc/services.d/nginx/run /etc/services.d/nginx/run-base && \  
# override nginx-start script to  
echo -e $(echo "\  
"#"!/bin/sh\\n\  
\\n\  
"#" clean up old links \\n\  
rm -rf /var/www/html \\n\  
"#" create softlink from html-base to html/some/url/root/of/adminer/ \\n\  
SUBDIR=\"\${ADMINER_SUBDIR:-/adminer/}\"\\n\  
if [ \"\${SUBDIR}\" = \"/\" ] \\n\  
then\\n\  
ln -s /var/www/html-base /var/www/html\\n\  
else \\n\  
DIR=\$(dirname \"\${SUBDIR}\")\\n\  
BASE=\$(basename \"\${SUBDIR}\")\\n\  
if [ \"\${DIR}\" = \".\" ]\\n\  
then \\n\  
ln -s /var/www/html-base /var/www/html\\n\  
else\\n\  
if [ \"\${DIR:0:1}\" = \"/\" ]\\n\  
then\\n\  
mkdir -p \"/var/www/html\${DIR}\"\\n\  
ln -s /var/www/html-base \"/var/www/html\${DIR}/\${BASE}\"\\n\  
else\\n\  
mkdir -p \"/var/www/html/\${DIR}\"\\n\  
ln -s /var/www/html-base \"/var/www/html/\${DIR}/\${BASE}\"\\n\  
fi\\n\  
fi\\n\  
fi\\n\  
\\n\  
"#" and then actually start nginx via base run\\n\  
exec /etc/services.d/nginx/run-base \\n\  
")> /etc/services.d/nginx/run && \  
chmod 755 /etc/services.d/nginx/run  

