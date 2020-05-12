def replace_domain(emial, old_domain,new_domain):
  if "@"+old_domain in email:
    index=email.index("@")
    new_email=email[:index]+"@"+new_domain
    return new_email
  return email

email="xyz@yahoo.com"
print(replace_domain(email,"yahoo.com","xyz.org"))
