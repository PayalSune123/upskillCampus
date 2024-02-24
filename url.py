import pyshorteners as ps

url="https://learn.upskillcampus.com/s/courses/656d72afe4b0c8074bb749cb/take"

u=ps.Shortener().tinyurl.short(url)

print(u)