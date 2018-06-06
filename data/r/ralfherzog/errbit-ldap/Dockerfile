FROM errbit/errbit:latest  
  
USER root  
  
# Trust my own services (does not work right not; seems to be a problem with
alpine linux)  
# COPY ./int.rherzog.de-CA.crt /usr/local/share/ca-
certificates/int.rherzog.de-CA.crt  
# RUN update-ca-certificates  
# Prepare installation of ldap auth gem  
RUN echo "gem 'devise_ldap_authenticatable'" >> Gemfile  
  
# We have to be root to install the net-ldap gem  
RUN bundle config --delete frozen && bundle install && bundle config --global
frozen 1  
  
USER errbit  
  
## Devise is already set up  
#RUN rails generate devise:install --skip  
#RUN rails generate devise user  
RUN rails generate devise_ldap_authenticatable:install  
  
# Tell devise to load ldap devise on startup  
RUN echo 'Errbit::Config.devise_modules << :ldap_authenticatable' >
config/initializers/devise_ldap.rb  
  
## Append method to User model  
# This returns the user.rb without the last 'end' instruction  
RUN head -n -1 app/models/user.rb > app/models/user.rb.tmp && \  
# Append the method to run before saving ldap user  
echo -e "\n def ldap_before_save\n\  
## May be your ldap configuration\n\  
# given_name = Devise::LDAP::Adapter.get_ldap_param(self.username,
'givenName')\n\  
# surname = Devise::LDAP::Adapter.get_ldap_param(self.username, 'sn')\n\  
mail = Devise::LDAP::Adapter.get_ldap_param(self.username, 'mail')\n\  
display_name = Devise::LDAP::Adapter.get_ldap_param(self.username,
'displayName')\n\  
\n\  
display_name = display_name.first if display_name.is_a? Array\n\  
mail = mail.first if mail.is_a? Array\n\  
\n\  
self.name = display_name\n\  
self.email = mail\n\  
end\n\  
end\n\  
" >> app/models/user.rb.tmp && \  
# Let the temporary file be the new production one  
mv app/models/user.rb.tmp app/models/user.rb  
  

