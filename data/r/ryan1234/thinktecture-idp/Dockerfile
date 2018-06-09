FROM microsoft/aspnet:1.0.0-beta4  
  
RUN mkdir -p /var/lib/dnx/idp  
ADD ./src /var/lib/dnx/idp  
RUN cd /var/lib/dnx/idp \  
&& dnu restore \  
&& cp Think*.dll ~/.dnx/packages/Thinktecture.IdentityServer3/1.5.0/lib/net45/
\  
&& cp System*.dll
~/.dnx/packages/System.IdentityModel.Tokens.Jwt/4.0.1/lib/net45/  
  
ENTRYPOINT ["dnx", "/var/lib/dnx/idp", "kestrel"]  

