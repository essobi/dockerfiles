FROM ansibleplaybookbundle/apb-base  
  
LABEL "com.redhat.apb.spec"=\  
"dmVyc2lvbjogMS4wCm5hbWU6IGthZmthLWFwYgpkZXNjcmlwdGlvbjogQVBCIGZvciBBcGFjaGUg\  
S2Fma2EgYW5kIEFwYWNoZSBab29rZWVwZXIKYmluZGFibGU6IEZhbHNlCmFzeW5jOiBvcHRpb25h\  
bAptZXRhZGF0YToKICBkaXNwbGF5TmFtZTogQXBhY2hlIEthZmthIENsdXN0ZXIKICBpbWFnZVVy\  
bDogImh0dHBzOi8vc3ZuLmFwYWNoZS5vcmcvcmVwb3MvYXNmL2thZmthL3NpdGUvbG9nb3Mva2Fm\  
a2EtbG9nby1uby10ZXh0LnBuZyIKICBkb2N1bWVudGF0aW9uVXJsOiAiaHR0cDovL2thZmthLmFw\  
YWNoZS5vcmcvZG9jdW1lbnRhdGlvbiIKICBwcm92aWRlckRpc3BsYXlOYW1lOiAiTWF0dGhpYXMg\  
V2Vzc2VuZG9yZiIKcGxhbnM6CiAgLSBuYW1lOiBkZWZhdWx0CiAgICBkZXNjcmlwdGlvbjogVGhp\  
cyBkZWZhdWx0IHBsYW4gZGVwbG95cyBrYWZrYS1hcGIKICAgIGZyZWU6IFRydWUKICAgIG1ldGFk\  
YXRhOiB7fQogICAgcGFyYW1ldGVyczogW10="  
  
COPY playbooks /opt/apb/actions  
COPY roles /opt/ansible/roles  
RUN chmod -R g=u /opt/{ansible,apb}  
USER apb  

