from faker import Factory
f = Factory.create()
ua = f.user_agent()
print(ua)