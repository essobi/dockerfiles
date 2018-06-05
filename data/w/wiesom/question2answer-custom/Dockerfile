FROM wiesom/question2answer:1.7.3  
  
## Install Plugins  
RUN q2a-install-plugin \  
kufeiko/QA-Google-Analytics-Plugin\  
NoahY/q2a-poll \  
NoahY/q2a-comment-voting \  
NoahY/q2a-badges \  
amiyasahu/q2a-syntax-highlighter \  
Towhidn/Q2A-feed-widget \  
wiesom/qa-behind-reverse-proxy-overrides  
  
  
## Replace editor with a new one  
ADD ckeditor*.zip /var/www/html/qa-plugin/wysiwyg-editor/ckeditor.zip  
ADD config.js /var/www/html/qa-plugin/wysiwyg-editor/ckeditor_config.js  
RUN rm -rf /var/www/html/qa-plugin/wysiwyg-editor/ckeditor && \  
cd /var/www/html/qa-plugin/wysiwyg-editor/ && \  
unzip ckeditor.zip && \  
rm -rf ckeditor.zip && \  
mv -f ckeditor_config.js ckeditor/config.js  
  

